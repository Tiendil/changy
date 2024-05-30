import datetime
import re
from pathlib import Path

import pydantic

from changy import constants as c
from changy.settings import settings

VERSION_DATETIME_FORMAT = "%Y-%m-%dT%H-%M-%S"
CHANGES_FILE_REGEX = re.compile(r"(\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2})_(.*)\.md")

workdir = Path.cwd()
configs_dir = workdir / settings.changelog_sources_dir

changelog_file = workdir / settings.changelog_name

header_file = configs_dir / settings.changelog_header
changes_template_file = configs_dir / settings.changes_file_template
unreleased_changes_file = configs_dir / settings.unreleased_changes_file
next_release_file = configs_dir / settings.next_release_changes_file


class Changes(pydantic.BaseModel):
    time: datetime.datetime
    version: str
    text: str

    @property
    def version_header(self) -> str:
        return f"{self.version} on {self.time.strftime('%Y-%m-%d')}"


def init() -> None:

    if configs_dir.exists():
        raise NotImplementedError("already initialized")

    configs_dir.mkdir()
    header_file.write_text(c.default_changelog_header)
    changes_template_file.write_text(c.default_change_file_template)

    create_unreleased()


def create_unreleased() -> None:
    unreleased_changes_file.write_text(c.default_change_file_template)


def approve_unreleased() -> None:
    if not unreleased_changes_file.exists():
        raise NotImplementedError("unreleased.md not found")

    unreleased_changes_file.rename(next_release_file)


def create_version(version: str) -> None:
    time = datetime.datetime.now().strftime(VERSION_DATETIME_FORMAT)

    version_file_name = f"{time}_{version}.md"

    next_version_file = configs_dir / version_file_name

    if not next_release_file.exists():
        raise NotImplementedError("next_release.md not found")

    next_release_file.rename(next_version_file)

    create_unreleased()


def create_changelog() -> None:

    if next_release_file.exists():
        raise NotImplementedError("Changelog is in process of updating, do something with next_release.md first")

    header = header_file.read_text()

    releases = []

    for file in configs_dir.iterdir():
        match = CHANGES_FILE_REGEX.match(file.name)

        if not match:
            continue

        time, version = match.groups()
        text = file.read_text()

        changes = Changes(time=datetime.datetime.strptime(time, VERSION_DATETIME_FORMAT), version=version, text=text)

        releases.append(changes)

    releases.sort(key=lambda x: x.time, reverse=True)

    content = [header]

    if unreleased_changes_file.exists():
        text = unreleased_changes_file.read_text()
        unreleased_text = text.format(version_header="Unreleased")
        content.append(unreleased_text)

    content.extend(change.text.format(version_header=change.version_header) for change in releases)

    content = [x.strip() for x in content]

    changelog_file.write_text("\n\n".join(content))
