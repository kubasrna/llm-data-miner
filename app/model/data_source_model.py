"""DataSourceModel"""
import torch

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class DataSourceModel:
    """ DataSourceModel class is responsible for handling data loading into the application"""

    def load_pdf_data(self, config):
        """function load pdf data loads data from all available PDF sources

        Args:
            config (_type_): program configuration
        """
        loader = DirectoryLoader(config.DATA_PATH,
                                 glob='*.pdf',
                                 loader_cls=PyPDFLoader)

        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=config.CHUNK_SIZE,
                                                       chunk_overlap=config.CHUNK_OVERLAP)
        texts = text_splitter.split_documents(documents)

        embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDINGS,
                                           model_kwargs={'device': "cuda" if torch.cuda.is_available() else "cpu"})

        vectorstore = FAISS.from_documents(texts, embeddings)
        vectorstore.save_local(config.DB_FAISS_PATH)
