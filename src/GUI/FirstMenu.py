from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox, QFrame, QSizePolicy
from PySide6.QtGui import QPalette, QPixmap
from PySide6.QtCore import Qt

from src.GFTemplate.GF_Tsundere import Tsundere
from src.GFTemplate.GF_Yandere import Yandere
from src.GUI.DiscussionMenu import DiscussionMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.discussion_menu = None
        self.setWindowTitle("AI Girlfriend")
        self.setGeometry(100, 100, 1000, 900)

        self.set_background("/Users/romainliefferinckx/PythonProjects/AIGF/ressources/background.jpg")

        self.context_choice = ""

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Mini-fenêtre centrée (le cadre pour les choix)
        mini_window = QFrame()
        mini_window.setStyleSheet("""
            QFrame {
                background-color: rgba(50, 50, 50, 1);
                border-radius: 15px;
                padding: 70;
                border: 2px solid rgba(255, 255, 255, 0.8);
            }
        """)
        mini_window.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Widgets internes
        self.choice_box = QComboBox()
        self.choice_box.addItems(["Shy", "Tsundere", "Normal"])

        self.choice_button = QPushButton("Select Personality")
        self.choice_button.clicked.connect(self.set_girlfriend_context)

        inner_layout = QVBoxLayout()
        inner_layout.addWidget(QLabel("Choose your girlfriend's personality:"))
        inner_layout.addWidget(self.choice_box)
        inner_layout.addWidget(self.choice_button)

        mini_window.setLayout(inner_layout)

        # Layout principal centré
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(mini_window, alignment=Qt.AlignCenter)
        main_layout.addStretch()

        central_widget.setLayout(main_layout)

    def set_girlfriend_context(self):
        choice = self.choice_box.currentText()
        if choice == "Shy":
            yandere = Yandere("Yandere")
            self.context_choice = yandere.get_context()
        elif choice == "Tsundere":
            tsundere = Tsundere("Tsundere")
            self.context_choice = tsundere.get_context()
        elif choice == "Normal":
            self.context_choice = ("You are my girlfriend Jade, answer my questions as Jade the girl"
                                   " who loves me, the assistant, only.")
        self.open_discussion_menu()

    def open_discussion_menu(self):
        if self.context_choice:
            self.discussion_menu = DiscussionMenu()
            self.discussion_menu.context_choice = self.context_choice
            self.discussion_menu.starting_discussion()
            self.discussion_menu.show()

    def set_background(self, image_path):
        self.setStyleSheet(f"""
            QMainWindow {{
                background-image: url({image_path});
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            }}
        """)
