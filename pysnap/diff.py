from difflib import Differ
from termcolor import colored

from .sorted_dict import SortedDict
from .formatter import Formatter


def format_line(line):
    line = line.rstrip('\n')
    if line.startswith('-'):
        return colored(line, 'green', attrs=['bold'])
    elif line.startswith('+'):
        return colored(line, 'red', attrs=['bold'])
    elif line.startswith('?'):
        return (
            colored('') +
            colored(line, 'yellow', attrs=['bold'])
        )

    return colored('') + colored(line, 'white', attrs=['dark'])


class PrettyDiff(object):
    def __init__(self, obj, pysnap):
        self.pretty = Formatter()
        self.differ = Differ()
        self.pysnap = pysnap
        if isinstance(obj, dict):
            obj = SortedDict(**obj)
        self.obj = self.pretty(obj)

    def __eq__(self, other):
        return isinstance(other, PrettyDiff) and self.obj == other.obj

    def __repr__(self):
        return repr(self.obj)

    def get_diff(self, other):
        text1 = ['Received ', ''] + self.pretty(self.obj).splitlines(1)
        text2 = ['Snapshot ', ''] + self.pretty(other).splitlines(1)

        lines = list(self.differ.compare(text2, text1))
        return [
            format_line(line) for line in lines
        ]
