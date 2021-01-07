import pathlib
import datetime
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
    / "Calendar"
)

TODAY = datetime.datetime.now()

FIXED = {
    "Today": TODAY,
    "Tomorrow": TODAY + datetime.timedelta(days=1),
    "Yesterday": TODAY - datetime.timedelta(days=1),
}

DTFORMAT = "%Y%m%d"


@decorators.jsonfilter
def main():
    dates = {}
    for path in sorted(NOTES.glob("*.md"), reverse=True)[:3]:
        dt = datetime.datetime.strptime(path.stem, DTFORMAT)
        dates[path.stem] = {
            "arg": "noteplan://x-callback-url/openNote?noteDate=" + path.stem,
            "title": dt.strftime("%Y%m%d"),
            "autocomplete": path.stem,
            "subtitle": dt.strftime("%Y-%m-%d"),
        }
    for title, dt in FIXED.items():
        key = dt.strftime("%Y%m%d")
        dates[key] = {
            "arg": "noteplan://x-callback-url/openNote?noteDate=" + key,
            "title": title,
            "autocomplete": title.lower(),
            "subtitle": dt.strftime("%Y-%m-%d"),
        }

    return dates.values()
