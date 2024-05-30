import datetime
from changy import constants as c


from pathlib import Path

from changy.settings import settings


workdir = Path.cwd()
configs_dir = workdir / settings.changelog_sources_dir

header_file = configs_dir / settings.changelog_header
changes_template_file = configs_dir / settings.changes_file_template
unreleased_changes_file = configs_dir / settings.unreleased_changes_file
next_release_file = configs_dir / settings.next_release_changes_file


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
    time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")

    version_file_name = f"{time}_{version}.md"

    next_version_file = configs_dir / version_file_name

    if not unreleased_changes_file.exists():
        raise NotImplementedError("unreleased.md not found")

    unreleased_changes_file.rename(next_version_file)

    create_unreleased()
