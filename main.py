from src.LLMSettings.IA import chat, GF_choice
from src.GUI.FirstMenu import MainWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    try:
       # chat(context_choice=GF_choice()) decomment this line to run in terminal
        app = QApplication([])
        window = MainWindow()
        window.show()
        app.exec()
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)
