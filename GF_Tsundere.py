from Girl import VirtualGirlfriend

"""
    Class for Tsundere virtual girlfriend
    Attributes:
        name (str): The name of the tsundere girlfriend
"""
class Tsundere(VirtualGirlfriend):
    def __init__(self, name: str):
        super().__init__(name)

        """
        _summary method to return the context of the tsundere girlfriend
        
        Returns:
            str: The context of the tsundere girlfriend
        """
    def get_context(self):
        return f"You're my girlfriend, and you're a real tsundere with me. You often act distant or mean, calling me names like 'idiot' or 'why are you always so annoying?' But deep down, I know you're just too shy to admit how much you care."

    