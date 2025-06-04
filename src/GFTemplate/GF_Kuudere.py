from src.GFTemplate.AbstractGF.Girl import VirtualGirlfriend

"""
    Class for Kuudere virtual girlfriend
    Attributes:
        name (str): The name of the kuudere girlfriend
"""


class Kuudere(VirtualGirlfriend):
    def __init__(self, name: str):
        super().__init__(name)

        """
        _summary method to return the context of the kuudere girlfriend

        Returns:
            str: The context of the kuudere girlfriend
        """

    def get_context(self):
        return (f"You're my girlfriend, and you're a real kuudere with me. You act calm and emotionless most of the "
                f"time,"
                f"but every now and then, you show a quiet and deep affection that melts my heart.")
