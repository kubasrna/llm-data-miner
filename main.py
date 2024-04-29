"""entry point to the application"""
import os
import sys

from app.controller.application_presenter import ApplicationPresenter
from app.model.config_model import ConfigModel
from app.model.data_source_model import DataSourceModel
from app.model.llm_model import LLMModel

if __name__ == "__main__":
    config_model = ConfigModel()
    data_source_model = DataSourceModel()
    llm_model = LLMModel()

    current_dir = os.path.realpath(__file__)
    presenter = ApplicationPresenter(
        config_model,
        data_source_model,
        llm_model)

    presenter.change_folder(current_dir)
    presenter.initialize_application()
    presenter.spin_up_prompt()
    presenter.shutdown()
