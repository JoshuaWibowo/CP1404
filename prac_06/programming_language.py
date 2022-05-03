"""CP1404/CP5632 Practical - Programming language class."""


class ProgrammingLanguage:
    """Represent programming language."""

    def __init__(self, field, typing, reflection, year):
        """Initialize a programming language information instance."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if programming language is dynamic."""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """Print format that gives programming language information."""
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
