"""ApplicationPresenter"""
import os

from torch import cuda

from app.model.config_model import ConfigModel
from app.model.data_source_model import DataSourceModel
from app.model.llm_model import LLMModel

class ApplicationPresenter:
    """Application presenter is central part of the MVP pattern."""

    def __init__(self, config_model: ConfigModel,
                 data_source_model: DataSourceModel,
                 llm_model: LLMModel) -> None:

        self.config_model = config_model
        self.data_source_model = data_source_model
        self.llm_model = llm_model
        self.view = main_window

    def change_folder(self, path: str) -> None:
        """changes directory to the main.py folder"""
        current_dir = os.path.dirname(path)
        os.chdir(current_dir)

    def initialize_application(self) -> None:
        """initializes the models, an observables to ui for the rest of the app"""
        self.config_model.load_config()
        self.config_model.update_config(
            "DEVICE", "cuda" if cuda.is_available() else "cpu")

        self.data_source_model.load_source_data(self.config_model.config)
        self.llm_model.scan_for_models()
        self.llm_model.start_model(self.config_model.config)

    def spin_up_prompt(self) -> None:
        """temporary function to get output from the model"""
        question = input("What do you want to know: ")
        while question != "stop":
            answer = self.llm_model.ask_question(question)
            print(answer['result'])
            question = input("What do you want to know: ")

    def shutdown(self) -> None:
        """graceful shutdown where updates of the config are saved"""
        self.config_model.save_config()
