"""Context module."""


class Context:
    """Context class which used to store/restore data.

    Note:
        This class defines ``__slots__`` attribute so sub-class must override
        the attribute to extend available attributes.

    Attributes:
        nvim (Nvim): The ``neovim.Nvim`` instance.
        text (str): A user input text of the prompt.
        caret_locus (int): A locus index of the caret in the prompt.

    """

    __slots__ = ('text', 'caret_locus')

    def __init__(self) -> None:
        """Constructor.

        Args:
            nvim (Nvim): The ``neovim.Nvim`` instance.

        """
        self.text = ''
        self.caret_locus = 0

    def to_dict(self) -> dict:
        """Convert a context instance into a dictionary.

        Use ``Context.from_dict(d)`` to restore a context instance from a
        dictionary.

        Returns:
            dict: A context dictionary.

        """
        return {
            k: getattr(self, k)
            for k in self.__slots__
        }

    @classmethod
    def from_dict(cls, d: dict) -> 'Context':
        """Create a new context instance from a dictionary.

        Use ``context.to_dict()`` to create a corresponding dictionary.

        Args:
            d (dict): A corresponding dictionary.

        Returns:
            Context: A context instance.
        """
        context = cls.__new__(cls)
        for k, v in d.items():
            if k in cls.__slots__:
                setattr(context, k, v)
        return context
