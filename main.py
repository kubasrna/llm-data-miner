"""entry point to the application"""
import os
import sys
from PyQt6.QtWidgets import QApplication

from app.controller.application_controller import ApplicationController
from app.ui.data_miner_llm import MainWindow



if __name__ == "__main__":
    current_dir = os.path.realpath(__file__)
    controller = ApplicationController()
    controller.change_folder(current_dir)

    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

    #controller.initialize_application()
    #controller.spin_up_prompt()
