import pyotp
import pyperclip
from pyguiadapter.interact import ulogging, upopup


def counterbased_otp(secret_key: str, counter: int = 0, copy_to_clipboard: bool = True):
    """
    Generate a counter-based One Time Password(OTP) from the given secret key.

    :param secret_key: <b>The secret key in base32</b>
    :param counter: <b>The OTP HMAC counter</b>
    :param copy_to_clipboard: <b> Whether copy the generated OPT to the system clipboard</b>
    :return:

    @widgets
    [secret_key]
    label="Secret Key"
    echo_mode="Password"
    clear_button=true
    placeholder="Input the secret key here"

    [counter]
    widget_class="IntSpinBox"
    label="Counter"
    min_value=0
    max_value=2147483647

    [copy_to_clipboard]
    widget_class="CheckBox"
    label=""
    text="Copy generated OTP to clipboard?"
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

