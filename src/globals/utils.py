import os
import platform


class Utils:
    @staticmethod
    def create_config_dir():
        # Check if the operating system is Linux

        if platform.system() == "Linux":
            sys_config_dir = os.path.join(os.path.expanduser("~"), ".config")
        elif platform.system() == "Windows":
            sys_config_dir = os.path.join(os.path.expanduser("~"), ".config")
        else:
            sys_config_dir = os.path.join(os.path.expanduser("~"), ".config")

        config_dir = os.path.join(sys_config_dir, "openai-client")
        history_dir = os.path.join(config_dir, 'history')
        settings_dir = os.path.join(config_dir, 'settings')
        media_dir = os.path.join(config_dir, 'media')
        media_images_dir = os.path.join(media_dir, 'images')
        memes_dir = os.path.join(media_images_dir, 'memes')
        dalle_dir = os.path.join(media_images_dir, 'dalle')

        # Check if the directory exists, and create it if it doesn't
        if not os.path.exists(sys_config_dir):
            os.makedirs(sys_config_dir)

        if not os.path.exists(config_dir):
            os.makedirs(config_dir)

        if not os.path.exists(history_dir):
            os.makedirs(history_dir)

        if not os.path.exists(settings_dir):
            os.makedirs(settings_dir)

        if not os.path.exists(media_dir):
            os.makedirs(media_dir)

        if not os.path.exists(media_images_dir):
            os.makedirs(media_images_dir)

        if not os.path.exists(memes_dir):
            os.makedirs(memes_dir)

        if not os.path.exists(dalle_dir):
            os.makedirs(dalle_dir)

    @staticmethod
    def get_config_dir():

        if platform.system() == "Linux":
            config_dir = os.path.join(os.path.expanduser("~"), ".config", "openai-client")
        elif platform.system() == "Windows":
            config_dir = os.path.join(os.path.expanduser("~"), ".config", "openai-client")
        else:
            config_dir = os.path.join(os.path.expanduser("~"), ".config", "openai-client")

        return config_dir

    @staticmethod
    def get_history_dir():

        config_dir = Utils.get_config_dir()
        history_dir = os.path.join(config_dir, 'history')
        return history_dir

    @staticmethod
    def get_settings_dir():

        config_dir = Utils.get_config_dir()
        settings_dir = os.path.join(config_dir, 'settings')
        return settings_dir

    @staticmethod
    def get_media_dir():

        config_dir = Utils.get_config_dir()
        media_dir = os.path.join(config_dir, 'media')
        return media_dir

    @staticmethod
    def get_media_images_dir():

        media_dir = Utils.get_media_dir()
        media_images_dir = os.path.join(media_dir, 'images')
        return media_images_dir

    @staticmethod
    def get_memes_dir():

        media_images_dir = Utils.get_media_images_dir()
        memes_dir = os.path.join(media_images_dir, 'memes')
        return memes_dir

    @staticmethod
    def get_dalle_dir():

        media_images_dir = Utils.get_media_images_dir()
        dalle_dir = os.path.join(media_images_dir, 'dalle')
        return dalle_dir

# @staticmethod
# def get_config_dir():
#     # Check if the operating system is Linux
#     if platform.system() == "Linux":
#
#         # Get the path to the openai-client directory
#         openai_client_dir = os.path.join(os.path.expanduser("~"), ".config", "openai-client")
#
#         return openai_client_dir
#     else:
#         print("This function is only supported on Linux.")
#         dirname = os.path.dirname(__file__)
#         return dirname
