import logging
import os

if os.environ.get("alfred_debug") == "1":
    logging.basicConfig(level=logging.DEBUG)
