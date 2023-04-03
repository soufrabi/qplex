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
        media_dir = os.path.join(config_dir, 'media')
        media_images_dir = os.path.join(media_dir,'images')
        memes_dir = os.path.join(media_images_dir, 'memes')

        # Check if the directory exists, and create it if it doesn't
        if not os.path.exists(sys_config_dir):
            os.makedirs(sys_config_dir)

        if not os.path.exists(config_dir):
            os.makedirs(config_dir)

        if not os.path.exists(media_dir):
            os.makedirs(media_dir)

        if not os.path.exists(media_images_dir):
            os.makedirs(media_images_dir)

        if not os.path.exists(memes_dir):
            os.makedirs(memes_dir)


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
    def get_media_dir():

        config_dir = Utils.get_config_dir()
        media_dir = os.path.join(config_dir, 'media')
        return media_dir

    @staticmethod
    def get_media_images_dir():

        media_dir = Utils.get_media_dir()
        media_images_dir = os.path.join(media_dir,'images')
        return media_images_dir

    @staticmethod
    def get_memes_dir():

        media_images_dir = Utils.get_media_images_dir()
        memes_dir = os.path.join(media_images_dir, 'memes')
        return memes_dir

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
