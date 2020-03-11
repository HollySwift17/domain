import re
import pygeoip
from termcolor import colored


def colored_label(label):
    return label
#return colored(label, 'yellow', attrs=['bold'])


def get_n_grams(n, string):
    if len(string) < n:
        return []
    result = list()
    for i in range(0, len(string) + 1 - n):
        n_gram = string[i:i + n]
        result.append(n_gram)

    return result


def clean_string(string):
    return string.strip().lower()


########################################
#Dictionary
########################################

class Dictionary(BaseException):
    __instance = None

    def __init__(self, dictionary_path='analysis/top10000en.txt'):
        if Dictionary.__instance:
            raise Dictionary.__instance

        Dictionary.__instance = self
        self._word_set = set()
        self._one_gram_dict = dict()
        self._two_gram_dict = dict()
        self._three_gram_dict = dict()
        self._four_gram_dict = dict()
        self._five_gram_dict = dict()

        with open(dictionary_path.strip(), 'r') as words_blob:
            for word in words_blob:
                regex = re.compile(r'[^a-z0-9]+')
                cleaned_word = regex.sub('', word)
#only lower number and apha

                self._word_set.add(cleaned_word)

                for one_gram in get_n_grams(1, cleaned_word):
                    if one_gram in self._one_gram_dict:
                        self._one_gram_dict[one_gram] = self._one_gram_dict[one_gram] + 1
                    else:
                        self._one_gram_dict[one_gram] = 1

                for two_gram in get_n_grams(2, cleaned_word):
                    if two_gram in self._two_gram_dict:
                        self._two_gram_dict[two_gram] = self._two_gram_dict[two_gram] + 1
                    else:
                        self._two_gram_dict[two_gram] = 1

                for three_gram in get_n_grams(3, cleaned_word):
                    if three_gram in self._three_gram_dict:
                        self._three_gram_dict[three_gram] = self._three_gram_dict[three_gram] + 1
                    else:
                        self._three_gram_dict[three_gram] = 1
                for four_gram in get_n_grams(4, cleaned_word):
                    if four_gram in self._four_gram_dict:
                        self._four_gram_dict[four_gram] = self._four_gram_dict[four_gram] + 1
                    else:
                        self._four_gram_dict[four_gram] = 1
                for five_gram in get_n_grams(5, cleaned_word):
                    if five_gram in self._five_gram_dict:
                        self._five_gram_dict[five_gram] = self._five_gram_dict[five_gram] + 1
                    else:
                        self._five_gram_dict[five_gram] = 1

    def is_word(self, candidate_word):
        return clean_string(candidate_word) in self._word_set

    def one_gram_count(self, one_gram):
        if one_gram in self._one_gram_dict:
            return self._one_gram_dict[one_gram]
        else:
            return 0

    def two_gram_count(self, two_gram):
        if two_gram in self._two_gram_dict:
            return self._two_gram_dict[two_gram]
        else:
            return 0

    def three_gram_count(self, three_gram):
        if three_gram in self._three_gram_dict:
            return self._three_gram_dict[three_gram]
        else:
            return 0

    def four_gram_count(self, four_gram):
        if four_gram in self._four_gram_dict:
            return self._four_gram_dict[four_gram]
        else:
            return 0

    def five_gram_count(self, five_gram):
        if five_gram in self._five_gram_dict:
            return self._five_gram_dict[five_gram]
        else:
            return 0

########################################
## Autonomous system database
########################################


class AutonomousSystemDatabase:
    __instance = None

    def __init__(self):
        if AutonomousSystemDatabase.__instance:
            raise AutonomousSystemDatabase.__instance

        AutonomousSystemDatabase.__instance = self
        self._as_db = pygeoip.GeoIP('dga_classifier/assets/GeoIPASNum.dat')

    def get_as_by_address(self, ip):
        result = self._as_db.org_by_addr(ip)

        if result == None:
            return 'Unknown Autonomous System'

        return result
