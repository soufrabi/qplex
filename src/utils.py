
import os
import platform

class Utils:
    @staticmethod
    def create_config_dir():
        # Check if the operating system is Linux
        if platform.system() == "Linux":

            # Get the path to the openai-client directory
            openai_client_dir = os.path.join(os.path.expanduser("~"), ".config", "openai-client")

            # Check if the ~/.config directory exists, and create it if it doesn't
            config_dir = os.path.join(os.path.expanduser("~"), ".config")
            if not os.path.exists(config_dir):
                os.makedirs(config_dir)

            # Check if the openai-client directory exists, and create it if it doesn't
            if not os.path.exists(openai_client_dir):
                os.makedirs(openai_client_dir)
                print(f"Created {openai_client_dir} directory.")
            else:
                print(f"{openai_client_dir} directory already exists.")
        else:
            print("This function is only supported on Linux.")
            return




    @staticmethod
    def get_config_dir():
        # Check if the operating system is Linux
        if platform.system() == "Linux":

            # Get the path to the openai-client directory
            openai_client_dir = os.path.join(os.path.expanduser("~"), ".config", "openai-client")

            return openai_client_dir
        else:
            print("This function is only supported on Linux.")
            dirname = os.path.dirname(__file__)
            return dirname

