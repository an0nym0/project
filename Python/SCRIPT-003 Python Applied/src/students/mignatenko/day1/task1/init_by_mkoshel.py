"""
Первая версия первого задания
"""
from collections import Counter
import timeit

from students.mignatenko.day1.task1.constants import TEXT, REPEAT_COUNT



def func():
    lower = TEXT.lower()
    return {
        'vovels': Counter(c for c in lower if c in 'aeiou'),
        'consonants': Counter(c for c in lower if c in 'bcdfghjklmnpqrstvwxyz')
    }
    # result['vowels'] = Counter(c for c in lower if c in 'aeiou')
    # result['consonants'] = Counter(c for c in lower if c in 'bcdfghjklmnpqrstvwxyz')
    return result


if __name__ == "__main__":

    r = timeit.Timer(func)
    print(r.timeit(REPEAT_COUNT))