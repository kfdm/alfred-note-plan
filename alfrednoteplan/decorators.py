import json
import sys


def jsonfilter(func):
    def inner():
        json.dump(({"items": list(func())}), fp=sys.stdout)

    return inner
