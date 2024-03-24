from pyguiadapter.adapter import GUIAdapter

import simple_otp.counterbased
import simple_otp.genkey
import simple_otp.timebased


def main():
    gui = GUIAdapter()

    gui.execution_window_config.show_function_result_dialog = False
    gui.execution_window_config.print_function_result = False
    gui.execution_window_config.print_function_started_info = False
    gui.execution_window_config.print_function_finished_info = False

    gui.execution_window_config.show_function_error_dialog = True
    gui.execution_window_config.function_error_dialog_message = "Error: {}"
    gui.execution_window_config.function_error_message = "Error: {}"

    gui.execution_window_config.auto_clear_output = False
    gui.selection_window_config.icon_mode = False

    gui.add(simple_otp.timebased.timebased_otp, display_name="Time-based OTP")
    gui.add(simple_otp.counterbased.counterbased_otp, display_name="Counter-based OTP", widgets_config={
        "counter": {
            "type": "IntSpinBox",
            "min_value": 0,
            "max_value": 2147483647,
        }
    })
    gui.add(simple_otp.genkey.generate_secret_key, display_name="Generate Secret Key")
    gui.run()


if __name__ == '__main__':
    main()
