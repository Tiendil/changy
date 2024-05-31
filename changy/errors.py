from typing import Any


class Error(Exception):
    message: str | None = None

    def __init__(self, **kwargs: Any) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

        # TODO: send to Sentry
        if "fingerprint" not in kwargs:
            self.fingerprint = None

        super().__init__(self.message or self.__class__.__name__)

    def __repr__(self) -> str:
        attributes = ", ".join(f"{key}={value}" for key, value in self.__dict__.items())

        return f"{self.__class__.__name__}: {attributes}"


class ChangyError(Error):
    pass


class ChangesDirDoesNotExist(ChangyError):
    message = "Changes directory does not exist"


class AlreadyInitialized(ChangyError):
    message = "Already initialized"


class NoApprovedChanges(ChangyError):
    message = "No approved changes found. Ensure you edited unreleased changes file and called `changy unrelease approve`."


class NoUnreleasedChanges(ChangyError):
    message = "No unreleased changes found. Ensure you finished updating the changelog and called `changy version create`."


class ApprovedChangesFileExists(ChangyError):
    message = "Approved changes file should not exist at this point. Ensure you finished version generation by calling `changy version create`."
