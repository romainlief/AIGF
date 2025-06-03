from PySide6.QtWidgets import QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QFrame, QSizePolicy, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
from src.LLMSettings.IA import chain
from src.GUI.AWindow.BaseWindow import BaseWindow


class DiscussionMenu(BaseWindow):
    def __init__(self):
        super().__init__()
        self.context_choice = ""

    def setup_ui(self):
        # ==== Création de la mini-fenêtre ====
        mini_window = QFrame()
        mini_window.setFixedSize(550, 500)
        mini_window.setStyleSheet("""
            QFrame {
                background-color: rgba(50, 50, 50, 1);
                border-radius: 15px;
                padding: 5px;
                border: 2px solid rgba(255, 255, 255, 0.8);
            }
        """)
        mini_window.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # ==== Widgets internes ====
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        self.chat_history.setFixedHeight(400)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message here...")
        self.input_field.setFixedWidth(500)
        self.input_field.setStyleSheet("""
            QLineEdit {
                background-color: rgba(180, 180, 180, 0.6);
                border: 2px solid rgba(50, 50, 50, 0.8);
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
                color: black;
            }
            QLineEdit:focus {
                border: 2px solid rgba(100, 150, 255, 0.8);
                background-color: rgba(230, 230, 230, 1);
            }
        """)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        # ==== Layout interne de la mini-fenêtre ====
        inner_layout = QVBoxLayout()
        inner_layout.addWidget(QLabel("Chat with your AI Girlfriend:"))
        inner_layout.addWidget(self.chat_history)
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_field, alignment=Qt.AlignCenter)
        inner_layout.addLayout(input_layout)
        inner_layout.addWidget(self.send_button)
        mini_window.setLayout(inner_layout)

        # ==== Layout principal centré ====
        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(mini_window, alignment=Qt.AlignCenter)
        main_layout.addStretch()

        self.central_widget.setLayout(main_layout)

    def starting_discussion(self):
        self.chat_history.append("Welcome to the AI Girlfriend Chat!")
        self.chat_history.append("You can quit the chat by typing 'quit' or 'exit'.")
        if self.context_choice == "Shy":
            self.chat_history.append("You selected the shy girlfriend.")
        elif self.context_choice == "Tsundere":
            self.chat_history.append("You selected the tsundere girlfriend.")
        elif self.context_choice == "Normal":
            self.chat_history.append("You selected the normal girlfriend.")

    def send_message(self):
        user_message = self.input_field.text()
        if user_message.strip():
            try:
                self.chat_history.append(f"You: {user_message}")
                result = chain.invoke({"context": self.context_choice, "question": user_message})
                self.chat_history.append(f"AI: {result}")
                self.context_choice += f"\nUser: {user_message}\nAI: {result}"
                self.input_field.clear()
            except Exception as e:
                self.chat_history.append(f"Error: {e}")
