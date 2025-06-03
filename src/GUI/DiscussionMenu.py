from PySide6.QtWidgets import QTextEdit, QLineEdit, QPushButton, QVBoxLayout
from src.LLMSettings.IA import chain
from src.GUI.AWindow.BaseWindow import BaseWindow


class DiscussionMenu(BaseWindow):
    def __init__(self):
        super().__init__()

    def setup_ui(self):
        self.context_choice = ""

        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message here...")

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        layout = QVBoxLayout()
        layout.addWidget(self.chat_history)
        layout.addWidget(self.input_field)
        layout.addWidget(self.send_button)
        self.central_widget.setLayout(layout)

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
