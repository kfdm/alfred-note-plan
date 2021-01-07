from alfrednoteplan import decorators, constants


@decorators.jsonfilter
def main():
    for path in constants.NOTES.glob("*.md"):
        with path.open() as fp:
            yield {
                "arg": "noteplan://x-callback-url/openNote?fileName=" + path.name,
                "title": path.stem,
                "autocomplete": path.stem,
                "subtitle": fp.readline(),
            }
