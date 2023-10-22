from typing import Any

from flask.helpers import (
    abort,
    flash,
    get_debug_flag,
    get_flashed_messages,
    get_load_dotenv,
    get_template_attribute,
    redirect,
    stream_with_context,
)
from quart.globals import current_app
from quart.helpers import (
    send_file as quart_send_file,
    send_from_directory as quart_send_from_directory,
)

from ._synchronise import sync_with_context


def url_for(*args: Any, **kwargs: Any) -> Any:
    return current_app.url_for(*args, **kwargs)


def make_response(*args: Any, **kwargs: Any) -> Any:
    return sync_with_context(current_app.make_response(*args, **kwargs))


def send_file(*args: Any, **kwargs: Any) -> Any:
    return sync_with_context(quart_send_file(*args, **kwargs))


def send_from_directory(*args: Any, **kwargs: Any) -> Any:
    return sync_with_context(quart_send_from_directory(*args, **kwargs))


__all__ = (
    "abort",
    "flash",
    "get_debug_flag",
    "get_flashed_messages",
    "get_load_dotenv",
    "get_template_attribute",
    "make_response",
    "redirect",
    "send_file",
    "send_from_directory",
    "stream_with_context",
    "url_for",
)
