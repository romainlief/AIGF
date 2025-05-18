from abc import ABC, abstractmethod

"""
    Abstract class for VirtualGirlfriend
    Attributes:
        name (str): The name of the virtual girlfriend
"""
class VirtualGirlfriend(ABC):
    def __init__(self, name: str):
        self.name = name

    """
    _summary method to return the context of the virtual girlfriend
    """
    @abstractmethod
    def get_context(self):
        pass

    