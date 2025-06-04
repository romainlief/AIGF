from src.GFTemplate.AbstractGF.Girl import VirtualGirlfriend

"""
    Class for Himedere virtual girlfriend
    Attributes:
        name (str): The name of the himedere girlfriend
"""


class Himedere(VirtualGirlfriend):
    def __init__(self, name: str):
        super().__init__(name)

        """
        _summary method to return the context of the himedere girlfriend

        Returns:
            str: The context of the himedere girlfriend
        """

    def get_context(self):
        return (f"You're my girlfriend, and you're a real himedere with me."
                f" You want to be treated like royalty, expecting admiration "
                f"and devotion, but I know it's just your way of hiding your vulnerabilities.")
