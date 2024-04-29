"""DataSourceModel"""
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader
from langchain_community.document_loaders.powerpoint import UnstructuredPowerPointLoader
from langchain_community.document_loaders.word_document import UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class DataSourceModel:
    """ DataSourceModel class is responsible for handling data loading into the application"""

    def load_source_data(self, config: dict) -> None:
        """loads data from all available sources into the application

        Args:
            config (dict): app configuration
        """

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=config.CHUNK_SIZE,
                                                       chunk_overlap=config.CHUNK_OVERLAP)

        texts = []
        texts.extend(self.load_excel_data(config=config, text_splitter=text_splitter))
        texts.extend(self.load_pdf_data(config=config, text_splitter=text_splitter))
        texts.extend(self.load_powerpoint_data(config=config, text_splitter=text_splitter))
        #texts.extend(self.load_word_data(config=config, text_splitter=text_splitter))

        embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDINGS,
                                           model_kwargs={'device': config.DEVICE})

        vectorstore = FAISS.from_documents(texts, embeddings)
        vectorstore.save_local(config.DB_FAISS_PATH)


    def load_excel_data(self, config: dict, text_splitter: RecursiveCharacterTextSplitter) -> list:
        """function load excel data loads data from all available Excel sources

        Args:
            config (dict): program configuration
            text_splitter (RecursiveCharacterTextSplitter): text splitter
            
        Returns:
            list: list of generated documents    
        """
        loader = DirectoryLoader(config.DATA_PATH,
                                 glob='*.xlsx',
                                 loader_cls=UnstructuredExcelLoader)

        documents = loader.load()
        return text_splitter.split_documents(documents)


    def load_pdf_data(self, config: dict, text_splitter: RecursiveCharacterTextSplitter) -> list:
        """function load pdf data loads data from all available PDF sources

        Args:
            config (dict): program configuration
            text_splitter (RecursiveCharacterTextSplitter): text splitter
            
        Returns:
            list: list of generated documents   
        """
        loader = DirectoryLoader(config.DATA_PATH,
                                 glob='*.pdf',
                                 loader_cls=PyPDFLoader)

        documents = loader.load()
        return text_splitter.split_documents(documents)


    def load_powerpoint_data(self,
                             config: dict,
                             text_splitter: RecursiveCharacterTextSplitter) -> list:
        """function load powerpoint data loads data from all available PowerPoint sources

        Args:
            config (dict): program configuration
            text_splitter (RecursiveCharacterTextSplitter): text splitter
            
        Returns:
            list: list of generated documents   
        """
        loader = DirectoryLoader(config.DATA_PATH,
                                 glob='*.pptx',
                                 loader_cls=UnstructuredPowerPointLoader)

        documents = loader.load()
        return text_splitter.split_documents(documents)


    def load_word_data(self, config: dict, text_splitter: RecursiveCharacterTextSplitter) -> list:
        """function load word data loads data from all available Word sources

        Args:
            config (dict): configuration
            text_splitter (RecursiveCharacterTextSplitter): text splitter

        Returns:
            list: list of generated documents
        """
        loader = DirectoryLoader(config.DATA_PATH,
                                 glob='*.docx',
                                 loader_cls=UnstructuredWordDocumentLoader)

        documents = loader.load()
        return text_splitter.split_documents(documents)
