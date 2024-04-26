"""ApplicationController"""
import os

from app.model.config_model import ConfigModel
from app.model.data_source_model import DataSourceModel
from app.model.llm_model import LLMModel

class ApplicationController:
    """Application controller is responsible distributing control inputs from the user"""

    def __init__(self) -> None:
        self.config_model = ConfigModel()
        self.llm_model = LLMModel()
        self.data_source_model = DataSourceModel()

    def change_folder(self, path: str) -> None:
        """changes directory to the main.py folder
        """
        current_dir = os.path.dirname(path)
        os.chdir(current_dir)

    def initialize_application(self) -> None:
        """initializes the model and rest of the app"""
        self.config_model.load_config()
        self.data_source_model.load_pdf_data(self.config_model.config)
        self.llm_model.scan_for_models()
        self.llm_model.start_model(self.config_model.config)

    def spin_up_prompt(self) -> None:
        """temporary function to get output from the model
        """
        questions = ""
        while questions != "stop":
            question = input("What do you want to know:")
            answer = self.llm_model.ask_question(question)
            print(answer['result'])
            