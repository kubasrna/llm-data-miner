"""DataMiner LLM main window"""
from PyQt6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    """Main window of the app"""

    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        """initializesUI"""
        