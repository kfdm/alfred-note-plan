import datetime
import sys
from urllib.parse import quote, urlencode

from alfrednoteplan import decorators

TODAY = datetime.datetime.now()
DTFORMAT = "%Y%m%d"


@decorators.jsonfilter
def main():
    text = " ".join(sys.argv[1:])
    yield {
        "arg": "noteplan://x-callback-url/addText?"
        + urlencode(
            {"noteDate": TODAY.strftime("%Y%m%d"), "text": "- " + text}, quote_via=quote
        ),
        "title": "Append new note",
        "subtitle": text,
    }
