from pyguiadapter.adapter import GUIAdapter

import simple_otp.counterbased
import simple_otp.genkey
import simple_otp.timebased


def main():
    gui = GUIAdapter()

    gui.execution_window_config.show_func_result_dialog = False
    gui.execution_window_config.print_func_result = False
    gui.execution_window_config.print_func_start_msg = False
    gui.execution_window_config.print_func_finish_msg = False

    gui.execution_window_config.print_func_error = True
    gui.execution_window_config.show_func_error_dialog = True

    gui.execution_window_config.autoclear_output = True
    gui.selection_window_config.icon_mode = False

    gui.add(simple_otp.timebased.timebased_otp, display_name="Time-based OTP")
    gui.add(simple_otp.counterbased.counterbased_otp, display_name="Counter-based OTP")
    gui.add(simple_otp.genkey.generate_secret_key, display_name="Generate Secret Key")
    gui.run()


if __name__ == '__main__':
    main()
