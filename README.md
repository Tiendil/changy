# Changy

Very simple changelog manager with the idea that changelogs are written by humans for humans.

Special message formatting (DSLs) to describe changes in commits, tags, etc. are good idea, but not very convinient for development and CI/CD process.

- The person who makes the commit is not always the person who are responsible for writing changelog or making release.
- The person who makes release also is not always responsible for writing changelog.
- The time when you want to work on changelog is not always the time when you are making commits or preparing release.
- Special message formatting is not always convinient for describing changes that will be read by humans.
- It is difficult to update messages in commit history.

I searched for tool that helps to manage changelogs but do not requires unnecessary effort from a developer, but did not find any. Thats how Changy was born.

Changy is inspired by:

- [Changie](https://github.com/miniscruff/changie)
- [Towncrier](https://github.com/twisted/towncrier)

But simpler, oriented on editing text files by hand: without cli commands to input changes, without strict messages format, etc.

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

Besides version files, there are some special files:

- `./changes/header.md` — content that will be placed at the top of the changelog.
- `./changes/changes_template.md` — template for version file. Changy will copy this file to create new version files.
- `./changes/unreleased.md` — changes that are not released yet.
- `./changes/next_release.md` — changes that are approved to the next release (see usage for details).

You should edit `./changes/unreleased.md` any time you want, before doing actual release. This file has no special syntax, but allows substitution of some variables:

- `{version_header}` — base header of version (version number + date).


# Usage

```bash
##################################
# Manual operations before release
##################################

# edit ./changes/unreleased.md

# This command should be run by hand before release to mark that changelog are reviewed by human and ready to be released.
changy unreleased approve

git commit -m "Approve changes for next release"

##################################
# Somewhere in you CI/CD pipeline
##################################

# For detailed exaxmple, see ./bin/prepate-release.sh

# creates version file with approved changes and creates new unreleased file
changy version create 1.2.3

# generates changelog
changy changelog create

git commit -m "Release 1.2.3"
```
