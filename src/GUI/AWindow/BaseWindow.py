from PySide6.QtWidgets import QMainWindow, QWidget


class BaseWindow(QMainWindow):
    DEFAULT_BACKGROUND = "/Users/romainliefferinckx/PythonProjects/AIGF/ressources/background.jpg"

    def __init__(self, title="AI Girlfriend", width=1000, height=900):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, width, height)

        self.set_background(self.DEFAULT_BACKGROUND)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.setup_ui()

    def set_background(self, image_path):
        self.setStyleSheet(f"""
            QMainWindow {{
                background-image: url({image_path});
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            }}
        """)

    def setup_ui(self):
        raise NotImplementedError("Subclasses must implement setup_ui()")
