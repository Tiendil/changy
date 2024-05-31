# Changy

Very simple changelog manager with the idea that humans write changelogs for humans, not for robots.

Special message formatting (DSLs) to describe changes in commits, tags, etc., is a good idea, but it is not always convenient for development and the CI/CD process.

- The person who commits is not always responsible for writing the changelog or making a release.
- The person who makes a release is also not always responsible for writing the changelog.
- The time when you want to work on the changelog is not always the time when you are making commits or preparing a release.
- Special message formatting is not always convenient for describing changes that humans will read.
- It is difficult to update messages in the commit history.

I searched for a tool that helps to manage changelogs but does not require unnecessary effort from a developer, but I did not find any that suited me. That's how Changy was born.

Changy is inspired by:

- [Changie](https://github.com/miniscruff/changie)
- [Towncrier](https://github.com/twisted/towncrier)

However, Changy simplifies the process by focusing on manual text file editing without the need for CLI commands or strict message formats.

# Installation

```bash
pip install changy

# create initial files
changy init

# help
changy help
```

# Idea

*All paths could be changed via environment variables. See ./changy/settings.py for deatils.*

`CHANGELOG.md` is compiled from parts from `./changes` directory: one file per version.

Besides version files, there are some particular files:

- `./changes/header.md` — Content placed at the top of the changelog.
- `./changes/changes_template.md` — Template for version files. Changy copies this file to create new version files.
- `./changes/unreleased.md` — Contains changes not yet released.
- `./changes/next_release.md` — Contains changes approved for the next release.

You may edit `./changes/unreleased.md` any time you want before making an actual release. The file has no special syntax.

# Usage

## Manual operations before release

```bash
# edit ./changes/unreleased.md

# This command should be run by the responsible person before release to mark that the changelog has been reviewed by humans and is ready to be released.
changy unreleased approve

git add -a
git commit -m "Approve changes for next release"
```

## Somewhere in your CI/CD pipeline

For detailed example, see ./bin/prepate-release.sh

```bash
# Creates version file with approved changes and creates new unreleased file
# Changy will fail if there are no approved changes => you will not forget to approve changes
changy version create 1.2.3

# generates changelog
changy changelog create

git add -a
git commit -m "Release 1.2.3"
```
