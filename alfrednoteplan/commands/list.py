import pathlib

from alfrednoteplan import decorators

NOTES = (
    pathlib.Path().home()
    / "Library"
    / "Containers"
    / "co.noteplan.NotePlan3"
    / "Data"
    / "Library"
    / "Application Support"
    / "co.noteplan.NotePlan3"
    / "Notes"
)


@decorators.jsonfilter
def main():
    for path in NOTES.glob("*.md"):
        yield {
            "arg": "noteplan://x-callback-url/openNote?fileName=" + path.name,
            "title": path.stem,
            "autocomplete": path.stem,
            "subtitle": str(path),
            "icon": {
                "type": "markdown",
            },
        }
