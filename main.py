"""entry point to the application"""
import os
import sys
from PyQt6.QtWidgets import QApplication

from app.controller.application_presenter import ApplicationPresenter
from app.model.config_model import ConfigModel
from app.model.data_source_model import DataSourceModel
from app.model.llm_model import LLMModel

from app.ui.data_miner_llm import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    config_model = ConfigModel()
    data_source_model = DataSourceModel()
    llm_model = LLMModel()

    main_window = MainWindow()

    current_dir = os.path.realpath(__file__)
    presenter = ApplicationPresenter(
        config_model,
        data_source_model,
        llm_model,
        main_window)

    presenter.change_folder(current_dir)
    presenter.initialize_application()
    presenter.spin_up_prompt()
    presenter.shutdown()
    #main_window.show()
    #sys.exit(app.exec())
