from typing import Literal

import pyotp
import pyperclip
from pyguiadapter.interact import upopup, ulogging


def generate_secret_key(secret_key_format: Literal["hex", "base64"] = "base64", copy_to_clipboard: bool = True):
    """
    Generate a secret key, compatible with Google Authenticator and other OTP apps.

    :param secret_key_format: generated key format, base32 or hex
    :param copy_to_clipboard: copy the generated OPT to the system clipboard
    :return:

    @widgets
    [secret_key_format]
    widget_class="ComboBox"
    label="Secret Key Format"

    [copy_to_clipboard]
    widget_class="CheckBox"
    label="Copy"
    text="Copy to clipboard"
    @end
    """
    secret_key_format = secret_key_format.lower()
    if secret_key_format not in ["hex", "base64"]:
        raise ValueError("secret_key_format must be 'hex' or 'base64'")
    if secret_key_format == "hex":
        key = pyotp.random_hex()
    else:
        key = pyotp.random_base32()
    ulogging.info(f"The secret key is generated: {key}", timestamp=True)
    upopup.information(f"The secret key is generated: {key}")
    if copy_to_clipboard:
        ulogging.info(f"Copying the secret key to the system clipboard...", timestamp=True)
        pyperclip.copy(key)
        ulogging.info(f"The secret key is copied to the system clipboard!", timestamp=True)
        upopup.information(f"The secret key is copied to the system clipboard!")
    return None
