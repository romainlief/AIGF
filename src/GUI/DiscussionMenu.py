from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox, QTextEdit, QLineEdit
from src.LLMSettings.IA import chain


class DiscussionMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Girlfriend")
        self.setGeometry(100, 100, 500, 400)

        # Chat context
        self.context_choice = ""

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a text area to display chat history
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)

        # Create a text input field for user messages
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message here...")

        # Create a button to send the message
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        layout = QVBoxLayout()
        layout.addWidget(self.chat_history)
        layout.addWidget(self.input_field)
        layout.addWidget(self.send_button)
        central_widget.setLayout(layout)

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
                # Append the user's message to the chat history
                self.chat_history.append(f"You: {user_message}")

                # Call the chat function and get the response
                result = chain.invoke({"context": self.context_choice, "question": user_message})

                # Append the AI's response to the chat history
                self.chat_history.append(f"AI: {result}")

                # Update the context with the new conversation
                self.context_choice += f"\nUser: {user_message}\nAI: {result}"
                self.input_field.clear()
            except Exception as e:
                self.chat_history.append(f"Error: {e}")