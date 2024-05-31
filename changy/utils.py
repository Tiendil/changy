import contextlib
import sys

from changy import errors


@contextlib.contextmanager
def exit_on_exception():
    try:
        yield
    except errors.ChangyError as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)
