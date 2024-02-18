"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder(list):
    """
    Takes in a path to a .txt file, converts each line into a word, and returns a list
    of those words.

    >>> wf = WordFinder('words.txt')
    >>> word = wf.random()
    >>> isinstance(word, str)
    True
    >>> word in wf
    True
    """
    def __init__(self, path):
        super().__init__()
        with open(path, 'r') as file:
            word_list = [line.strip() for line in file.readlines()]
        self.extend(word_list)

    def __repr__(self):
        return f"{len(self)} words read"
    
    def random(self):
        """Chooses a word from the list at random and returns that word."""
        return random.choice(self)

finder = WordFinder('words.txt')

print(f'''
{finder}

Random words:
{finder.random()}
{finder.random()}
{finder.random()}
{finder.random()}
{finder.random()}
{finder.random()}
{finder.random()}
''')

class SpecialWordFinder(WordFinder):
    """
    Takes in a path to a .txt file, converts each line into a word, and returns a list of
    those words.

    Takes care to exclude blank lines and comment lines (beginning with #)

    >>> swf = SpecialWordFinder('special.txt')
    >>> word = swf.random()
    >>> isinstance(word, str)
    True
    >>> word in swf
    True
    """
    def __init__(self, path):
        super().__init__(path)
        with open(path, 'r') as file:
            word_list = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        self.extend(word_list)

special = SpecialWordFinder('special.txt')

print(f'''
{special}

Random words:
{special.random()}
{special.random()}
{special.random()}
{special.random()}
{special.random()}
{special.random()}
{special.random()}
''')