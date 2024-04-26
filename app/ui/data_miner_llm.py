"""DataMiner LLM main window"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


class MainWindow(QWidget):
    """Main window of the app"""

    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        """initializesUI"""
        # Create widgets
        label = QLabel('Hello, PyQt6!')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(label)

        # Set the layout
        self.setLayout(layout)

        # Set window title and size
        self.setWindowTitle('My PyQt6 App')
        self.resize(300, 200)
