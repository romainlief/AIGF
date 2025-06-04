from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QComboBox, QFrame, QSizePolicy
from PySide6.QtCore import Qt

from src.GFTemplate.GF_Tsundere import Tsundere
from src.GFTemplate.GF_Yandere import Yandere
from src.GFTemplate.GF_Dandere import Dandere
from src.GFTemplate.GF_Kuudere import Kuudere
from src.GFTemplate.GF_Deredere import Deredere
from src.GFTemplate.GF_Himedere import Himedere
from src.GUI.DiscussionMenu import DiscussionMenu
from src.GUI.AWindow.BaseWindow import BaseWindow


class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.discussion_menu = None
        self.context_choice = ""

    def setup_ui(self):
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

        self.choice_box = QComboBox()
        self.choice_box.addItems(["Shy", "Tsundere", "Himedere", "Dandere", "Kuudere", "Deredere"])


        self.choice_button = QPushButton("Select Personality")
        self.choice_button.clicked.connect(self.set_girlfriend_context)

        inner_layout = QVBoxLayout()
        inner_layout.addWidget(QLabel("Choose your girlfriend's personality:"))
        inner_layout.addWidget(self.choice_box)
        inner_layout.addWidget(self.choice_button)
        mini_window.setLayout(inner_layout)

        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(mini_window, alignment=Qt.AlignCenter)
        main_layout.addStretch()

        self.central_widget.setLayout(main_layout)

    def set_girlfriend_context(self):
        choice = self.choice_box.currentText()
        if choice == "Shy":
            yandere = Yandere("Yandere")
            self.context_choice = yandere.get_context()
        elif choice == "Tsundere":
            tsundere = Tsundere("Tsundere")
            self.context_choice = tsundere.get_context()
        elif choice == "Himedere":
            himedere = Himedere("Himedere")
            self.context_choice = himedere.get_context()
        elif choice == "Dandere":
            dandere = Dandere("Dandere")
            self.context_choice = dandere.get_context()
        elif choice == "Kuudere":
            kuudere = Kuudere("Kuudere")
            self.context_choice = kuudere.get_context()
        elif choice == "Deredere":
            deredere = Deredere("Deredere")
            self.context_choice = deredere.get_context()
        self.open_discussion_menu()

    def open_discussion_menu(self):
        if self.context_choice:
            self.discussion_menu = DiscussionMenu()
            self.discussion_menu.context_choice = self.context_choice
            self.hide()
            self.discussion_menu.closed_signal.connect(self.show)
            self.discussion_menu.starting_discussion()
            self.discussion_menu.show()

