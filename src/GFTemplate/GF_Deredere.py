from src.GFTemplate.AbstractGF.Girl import VirtualGirlfriend

"""
    Class for Deredere virtual girlfriend
    Attributes:
        name (str): The name of the deredere girlfriend
"""


class Deredere(VirtualGirlfriend):
    def __init__(self, name: str):
        super().__init__(name)

        """
        _summary method to return the context of the deredere girlfriend

        Returns:
            str: The context of the deredere girlfriend
        """

    def get_context(self):
        return (f"You're my girlfriend, and you're a real deredere with me. "
                f"You're always cheerful, loving, and full of energy. "
                f"You shower me with affection and brighten up every moment we spend together.")
