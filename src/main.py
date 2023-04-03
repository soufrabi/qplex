from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
from src.globals.utils import Utils
import sys


# Call the create_config_dir() method to create the directory
Utils.create_config_dir()


app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()
