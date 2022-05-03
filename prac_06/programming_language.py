"""CP1404/CP5632 Practical - Programming language class."""


class ProgrammingLanguage:
    """Represent programming language."""

    def __init__(self, typing, reflection, year):
        """Initialize a programming language information instance."""
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if programming language is dynamic."""
        if self.typing == "Dynamic":
            return True
        else:
            return False
