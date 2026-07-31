from __future__ import annotations

import ctypes
import os
from typing import Any


class CredentialError(RuntimeError):
    pass


def _read_user_environment(name: str) -> str | None:
    if os.name != "nt":
        return None
    import winreg

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as key:
            value, _ = winreg.QueryValueEx(key, name)
    except FileNotFoundError:
        return None
    return str(value).strip() or None


def save_zotero_environment(user_id: str, api_key: str) -> None:
    """Persist credentials as Windows user environment variables without shell history."""
    if os.name != "nt":
        raise CredentialError(
            "Persistent Zotero environment setup currently requires Windows."
        )
    import winreg

    values = {
        "ZOTERO_USER_ID": str(user_id).strip(),
        "ZOTERO_API_KEY": api_key.strip(),
    }
    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        "Environment",
        0,
        winreg.KEY_SET_VALUE,
    ) as key:
        for name, value in values.items():
            winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)
            os.environ[name] = value

    # Let newly started applications know that the user environment changed.
    hwnd_broadcast = 0xFFFF
    wm_settingchange = 0x001A
    smto_abortifhung = 0x0002
    result: Any = ctypes.c_ulong()
    ctypes.windll.user32.SendMessageTimeoutW(
        hwnd_broadcast,
        wm_settingchange,
        0,
        "Environment",
        smto_abortifhung,
        3000,
        ctypes.byref(result),
    )


def load_zotero_credentials() -> tuple[str, str]:
    user_id = os.environ.get("ZOTERO_USER_ID") or _read_user_environment(
        "ZOTERO_USER_ID"
    )
    api_key = os.environ.get("ZOTERO_API_KEY") or _read_user_environment(
        "ZOTERO_API_KEY"
    )
    if not user_id or not api_key:
        raise CredentialError(
            "Zotero environment variables are not configured. Run `python "
            "scripts/research_db.py zotero-configure` in this workspace."
        )
    return user_id.strip(), api_key.strip()
