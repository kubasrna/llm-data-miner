"""LLMModel"""
import os
import torch

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms.ctransformers import CTransformers
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.chains.retrieval_qa.base import RetrievalQA


class LLMModel:
    """class LLMModel contains all information 
    about available models and is entry point to interact with them
    """

    def __init__(self) -> None:
        self.models = None
        self.active_model = None
        self.qa_prompt = None

        self.qa_template = """
        Use the following pieces of information to answer the user's question.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        Context: {context}
        Question: {question}

        Only return the helpful answer below and nothing else.
        Helpful answer:
        """
        self.qa_chain = None

    def scan_for_models(self) -> None:
        """function scan for models tries to find all models which given app can use

        Returns:
            list: paths to all given files
        """
        extension = ".gguf"
        folder_path = "models"
        file_list = []
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(extension):
                    file_list.append(os.path.join(root, file))
        self.models = file_list

    def start_model(self, config) -> None:
        """start model is function responsible for spinning up specific model

        Args:
            config (_type_): configuration provided by the user
        """
        self.active_model = CTransformers(model=self.models[0],
                                          model_type=config.MODEL_TYPE,
                                          max_new_tokens=config.MAX_NEW_TOKENS,
                                          temperature=config.TEMPERATURE)

        self.qa_prompt = PromptTemplate.from_template(self.qa_template)
        self.qa_prompt.input_variables = ['context', 'question']

        embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDINGS,
                                           model_kwargs={'device': config.DEVICE})

        vectordb = FAISS.load_local(
            config.DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)

        retriever = vectordb.as_retriever(
            search_kwargs={'k': config.VECTOR_COUNT})

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.active_model,
            chain_type='stuff',
            retriever=retriever,
            return_source_documents=config.RETURN_SOURCE_DOCUMENTS,
            chain_type_kwargs={'prompt': self.qa_prompt})

    def ask_question(self, question: str) -> str:
        """ ask question queries the LLM for answer based on the data

        Args:
            question (str): question for the data

        Returns:
            str: answer to the question
        """
        return self.qa_chain.invoke({'query': question})
