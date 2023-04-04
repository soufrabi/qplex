from PySide6.QtWidgets import QFileDialog, QMessageBox


class Popups:

    @staticmethod
    def get_path_dir():
        # Open a directory dialog and get the path to the selected directory
        dir_path = QFileDialog.getExistingDirectory(
            None,  # Parent widget (or None)
            "Select a directory",  # Dialog title
            "",  # Starting directory (optional)
        )

        # Print the selected directory path
        print("Selected directory:", dir_path)
        return dir_path

    @staticmethod
    def get_confirmation(window_title, text, informative_text):
        message = QMessageBox()
        message.setMinimumSize(700, 300)
        message.setWindowTitle(window_title)

        message.setText(text)
        message.setInformativeText(informative_text)
        # message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Cancel)

        # Show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
            return True
        elif ret == QMessageBox.Cancel:
            print("User chose Cancel")
            return False
        else:
            print("User chose unknown button")
            return False
