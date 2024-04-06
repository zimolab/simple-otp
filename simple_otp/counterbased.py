import pyotp
import pyperclip
from pyguiadapter.interact import ulogging, upopup


def counterbased_otp(secret_key: str, counter: int = 0, copy_to_clipboard: bool = True):
    """
    Generate a counter-based One Time Password(OTP) from the given secret key.

    :param secret_key: the secret key in base32
    :param counter: the OTP HMAC counter
    :param copy_to_clipboard: copy the generated OTP to the system clipboard
    :return:

    @widgets
    [secret_key]
    widget_class="LineEdit"
    label="Secret Key"
    echo_mode="Password"
    clear_button=true
    placeholder="input the secret you here"

    [copy_to_clipboard]
    widget_class="CheckBox"
    label="Copy"
    text="Copy to clipboard"

    [counter]
    widget_class="IntSpinBox"
    label="Counter"
    min_value=0
    max_value=2147483647
    @end
    """
    if not secret_key:
        msg = "The secret key is empty! Please input the secret key!"
        ulogging.warning(msg, timestamp=True)
        upopup.warning(msg)
        return
    if counter < 0:
        msg = "The counter is less than 0! Please input a valid counter!"
        ulogging.warning(msg, timestamp=True)
        upopup.warning(msg)
        return
    otp = pyotp.HOTP(secret_key)
    otp_str = otp.at(counter)
    ulogging.info(f"The OTP is generated: {otp_str}", timestamp=True)
    upopup.information(f"The OTP is generated: {otp_str}")
    if copy_to_clipboard:
        ulogging.info(f"Copying the OTP to the system clipboard...", timestamp=True)
        pyperclip.copy(otp_str)
        ulogging.info(f"The OTP is copied to the system clipboard!", timestamp=True)
        upopup.information(f"The OTP is copied to the system clipboard!")
    return None

