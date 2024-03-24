import pyotp
import pyperclip
from pyguiadapter.interact import ulogging, upopup


def timebased_otp(secret_key: str, copy_to_clipboard: bool = True):
    """
    Generate a time-based One Time Password(OTP) from the given secret key.

    :param secret_key: <b>The secret key in base32</b>
    :param copy_to_clipboard: <b> Whether copy the generated OPT to the system clipboard</b>
    :return:

    @begin
    [secret_key]
    type="LineEdit"
    label="Secret Key"
    echo_mode="Password"
    clear_button=true
    placeholder="input the secret you here"

    [copy_to_clipboard]
    type="CheckBox"
    label="Copy"
    text="Copy generated OTP to clipboard?"
    @end
    """
    if not secret_key:
        msg = "The secret key is empty! Please input the secret key!"
        ulogging.warning(msg, timestamp=True)
        upopup.warning(msg)
        return
    ulogging.info(f"Generating OTP for the secret key...", timestamp=True)
    otp = pyotp.TOTP(secret_key)
    otp_str = otp.now()
    ulogging.info(f"The OTP is generated: {otp_str}", timestamp=True)
    upopup.information(f"The OTP is generated: {otp_str}")
    if copy_to_clipboard:
        ulogging.info(f"Copying the OTP to the system clipboard...", timestamp=True)
        pyperclip.copy(otp_str)
        ulogging.info(f"The OTP is copied to the system clipboard!", timestamp=True)
        upopup.information(f"The OTP is copied to the system clipboard!")
    return None
