import re
from statistics import median


class Words:
    splitters: str = r"\, |\. |\; |\! |\? |\... |\ |\!|\.|\?|\...|\,|\;"
    def __init__(self, str_input: str, K: int, N: int):
        self.str_input: str = str_input
        self.K: int = K
        self.N: int = N
        self.str: str = ""
        self.word_dict: dict = {}
        self.ngrams_dict: dict = {}

    def count_words(self):
        self.str = re.split(self.splitters, self.str_input)
        self.check_empty()
        for key in self.str:
            if not self.word_dict.get(key):
                self.word_dict[key] = 1
            else:
                self.word_dict[key] += 1

    def print_dict(self):
        print(self.word_dict)

    def check_empty(self):
        if self.str.__contains__(''):
            self.str.remove('')

    def fdmedian(self) -> float:
        return median(self.word_dict.values())

    def average(self) -> float:
        return (len(self.str) / (self.str_input.count('!') + self.str_input.count('.') + self.str_input.count('?')))

    def ngramms(self):
        new_str = ''
        for i in range(len(self.str)):
            new_str += self.str[i]
        for i in range(len(new_str)):
            if (i + self.N) > len(new_str):
                break
            ng = new_str[i:i + self.N]
            if not self.ngrams_dict.get(ng):
                self.ngrams_dict[ng] = 1
            else:
                self.ngrams_dict[ng] += 1

    def top_k(self):
        sorted_dict = dict()
        sorted_keys = sorted(self.ngrams_dict, key=self.ngrams_dict.get, reverse=True)
        k = 0
        for key in sorted_keys:
            sorted_dict[key] = self.ngrams_dict[key]
        for key in sorted_keys:
            print(key, sorted_dict[key])
            if k == self.K:
                break
            k += 1