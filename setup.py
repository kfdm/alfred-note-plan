from setuptools import find_packages, setup

setup(
    name="alfred-note-plan",
    entry_points={
        "console_scripts": [
            "noteplan-list = alfrednoteplan.commands.list:main",
            "noteplan-date = alfrednoteplan.commands.date:main",
            "noteplan-log = alfrednoteplan.commands.log:main",
        ],
    },
)
