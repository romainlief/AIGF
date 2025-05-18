from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox, QTextEdit, QLineEdit
from src.GFTemplate.GF_Tsundere import Tsundere
from src.GFTemplate.GF_Yandere import Yandere
from src.GUI.DiscussionMenu import DiscussionMenu

"""
    Main window class for the GUI application
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Girlfriend")
        self.setGeometry(100, 100, 500, 400)

        # Chat context
        self.context_choice = ""

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a dropdown for girlfriend personality selection
        self.choice_box = QComboBox()
        self.choice_box.addItems(["Shy", "Tsundere", "Normal"])

        # Create a button to confirm the choice
        self.choice_button = QPushButton("Select Personality")
        self.choice_button.clicked.connect(self.set_girlfriend_context)



        # Create a layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Choose your girlfriend's personality:"))
        layout.addWidget(self.choice_box)
        layout.addWidget(self.choice_button)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

    def set_girlfriend_context(self):
        choice = self.choice_box.currentText()
        if choice == "Shy":
            yandere = Yandere("Yandere")
            self.context_choice = yandere.get_context()
        elif choice == "Tsundere":
            tsundere = Tsundere("Tsundere")
            self.context_choice = tsundere.get_context()
        elif choice == "Normal":
            self.context_choice = "You are my girlfriend Jade, answer my questions as Jade the girl who loves me, the assistant, only."
        self.open_discussion_menu()

    def open_discussion_menu(self):
        if self.context_choice:  # Ensure a context is selected
            self.discussion_menu = DiscussionMenu()
            self.discussion_menu.context_choice = self.context_choice
            self.discussion_menu.starting_discussion()
            self.discussion_menu.show()