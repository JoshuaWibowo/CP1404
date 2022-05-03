"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class."""
from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    programming_languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for pl in programming_languages:  # pl stands for programming language
        if pl.is_dynamic():
            print(pl.field)


main()
