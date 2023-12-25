import sys
import os
import platform


class Utils:
    def __init__(self):
        # Check if the operating system is Linux

        self.package_name = "qplex"

        def get_valid_path(env_var, fallback_dir)->str:
            path = os.getenv(env_var)
            if path and os.path.exists(path) and os.path.isdir(path):
                return path
            return fallback_dir

        if platform.system() == "Linux":

            fallback_config_dir = os.path.join(os.path.expanduser("~"), ".config")
            fallback_data_dir = os.path.join(os.path.expanduser("~"), ".local", "share")
            fallback_cache_dir = os.path.join(os.path.expanduser("~"), ".cache")

            self.sys_config_dir = get_valid_path('XDG_CONFIG_HOME', fallback_config_dir)
            self.sys_data_dir = get_valid_path('XDG_DATA_HOME', fallback_data_dir)
            self.sys_cache_dir = get_valid_path('XDG_CACHE_HOME', fallback_cache_dir)


        elif platform.system() == "Windows":
            fallback_config_dir = os.path.join(os.path.expanduser("~"), ".config")
            fallback_data_dir = os.path.join(os.path.expanduser("~"), ".local", "share")
            fallback_cache_dir = os.path.join(os.path.expanduser("~"), ".cache")

            self.sys_config_dir = get_valid_path('XDG_CONFIG_HOME', fallback_config_dir)
            self.sys_data_dir = get_valid_path('XDG_DATA_HOME', fallback_data_dir)
            self.sys_cache_dir = get_valid_path('XDG_CACHE_HOME', fallback_cache_dir)
        else:
            fallback_config_dir = os.path.join(os.path.expanduser("~"), ".config")
            fallback_data_dir = os.path.join(os.path.expanduser("~"), ".local", "share")
            fallback_cache_dir = os.path.join(os.path.expanduser("~"), ".cache")

            self.sys_config_dir = get_valid_path('XDG_CONFIG_HOME', fallback_config_dir)
            self.sys_data_dir = get_valid_path('XDG_DATA_HOME', fallback_data_dir)
            self.sys_cache_dir = get_valid_path('XDG_CACHE_HOME', fallback_cache_dir)

        print("sys_config_dir:", self.sys_config_dir)
        print("sys_data_dir:", self.sys_data_dir)
        print("sys_cache_dir:", self.sys_cache_dir)

        self.config_dir = os.path.join(self.sys_config_dir, self.package_name)
        self.data_dir = os.path.join(self.sys_data_dir, self.package_name)
        self.cache_dir = os.path.join(self.sys_cache_dir, self.package_name)

        self.history_dir = os.path.join(self.cache_dir, 'history')
        self.settings_dir = os.path.join(self.cache_dir, 'settings')
        self.media_dir = os.path.join(self.cache_dir, 'media')
        self.media_images_dir = os.path.join(self.media_dir, 'images')
        self.memes_dir = os.path.join(self.media_images_dir, 'memes')
        self.dalle_dir = os.path.join(self.media_images_dir, 'dalle')

        # Check if the directory exists, and create it if it doesn't
        os.makedirs(self.sys_config_dir,exist_ok=True )
        os.makedirs(self.sys_data_dir,exist_ok=True)
        os.makedirs(self.sys_cache_dir,exist_ok=True)

        os.makedirs(self.config_dir,exist_ok=True)
        os.makedirs(self.data_dir,exist_ok=True)
        os.makedirs(self.cache_dir,exist_ok=True)

        os.makedirs(self.history_dir,exist_ok=True)

        os.makedirs(self.settings_dir,exist_ok=True)

        os.makedirs(self.media_dir,exist_ok=True)

        os.makedirs(self.media_images_dir,exist_ok=True)

        os.makedirs(self.memes_dir,exist_ok=True)

        os.makedirs(self.dalle_dir,exist_ok=True)

    def get_config_dir(self,):

        if platform.system() == "Linux":
            config_dir = os.path.join(os.path.expanduser("~"), ".config", self.package_name)
        elif platform.system() == "Windows":
            config_dir = os.path.join(os.path.expanduser("~"), ".config", self.package_name)
        else:
            config_dir = os.path.join(os.path.expanduser("~"), ".config", self.package_name)

        return config_dir

    def get_history_dir(self):

        return self.history_dir

    def get_settings_dir(self):

        return self.settings_dir

    def get_media_dir(self):

        return self.media_dir

    def get_media_images_dir(self):

        return self.media_images_dir

    def get_memes_dir(self):

        return self.memes_dir

    def get_dalle_dir(self):

        return self.dalle_dir

    def empty_dir(self,dir_path):

        print("Delete contents of "+dir_path)
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

    # https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
    def resource_path(self,*args:str)->str:
        """ Get absolute path to resource, works for dev and for PyInstaller """

        relative_path:str = os.path.join(*args)
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
            # base_path = sys._MEIPASS2
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)





