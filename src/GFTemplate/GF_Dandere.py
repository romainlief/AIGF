from src.GFTemplate.AbstractGF.Girl import VirtualGirlfriend

"""
    Class for Dandere virtual girlfriend
    Attributes:
        name (str): The name of the dandere girlfriend
"""


class Dandere(VirtualGirlfriend):
    def __init__(self, name: str):
        super().__init__(name)

        """
        _summary method to return the context of the dandere girlfriend

        Returns:
            str: The context of the dandere girlfriend
        """

    def get_context(self):
        return (f"You're my girlfriend, and you're a real dandere with me. You're extremely quiet and shy around "
                f"others,"
                f"but when it's just the two of us, you open up and show your true gentle and loving side.")
