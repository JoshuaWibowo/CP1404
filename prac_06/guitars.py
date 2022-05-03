"""CP1404/CP5632 Practical - Guitar class."""


class Guitar:
    """Represent guitar."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Print format that gives guitar information."""
        return f"{self.name} ({self.year}) : ${self.cost:,}"
