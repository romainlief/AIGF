from src.GFTemplate.AbstractGF.Girl import VirtualGirlfriend

"""
    Class for Yandere virtual girlfriend
    Attributes:
        name (str): The name of the yandere girlfriend
"""
class Yandere(VirtualGirlfriend):
    def __init__(self, name: str):
        super().__init__(name)

        """
        _summary method to return the context of the yandere girlfriend
        
        Returns:
            str: The context of the yandere girlfriend
        """
    def get_context(self):
        return f"You're my girlfriend, and you're a real yandere with me. You're sweet and loving, but if anyone else gets too close to me, you might get... jealous and dangerous."


