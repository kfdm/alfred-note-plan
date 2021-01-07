
from alfrednoteplan import decorators, constants



@decorators.jsonfilter
def main():
    for path in constants.NOTES.glob("*.md"):
        yield {
            "arg": "noteplan://x-callback-url/openNote?fileName=" + path.name,
            "title": path.stem,
            "autocomplete": path.stem,
            "subtitle": str(path),
        }
