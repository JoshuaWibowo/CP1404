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

    def get_age(self):
        """Get guitar age."""
        return 2022 - self.year

    def is_vintage(self):
        """Determine if guitar is vintage."""
        if self.get_age() >= 50:
            return True
        else:
            return False
