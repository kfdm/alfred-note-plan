import json
import logging
import sys
import time

logger = logging.getLogger(__name__)


def jsonfilter(func):
    def inner():
        start = time.time()
        json.dump(({"items": list(func())}), fp=sys.stdout)
        end = time.time()
        logger.debug("Script took %s", end - start)

    return inner
