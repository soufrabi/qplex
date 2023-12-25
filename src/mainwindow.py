from PySide6.QtCore import  QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar
from src.text_main_widget import TextMainWidget
from src.central_widget import CentralWidget
from src.menu_bar_main import MenuBarMain
from src.status_bar_main import StatusBarMain
from src.toolbar_main import ToolBarMain

class MainWindow (QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app # declare an app window
        self.setWindowTitle("QPlex")

        # Central Widget
        central_widget = CentralWidget()

        # Working with Status Bar
        status_bar = StatusBarMain()
        self.setStatusBar(status_bar)

        # Menubar and menus
        menu_bar = MenuBarMain(app,central_widget.widget_text,status_bar)
        self.setMenuBar(menu_bar)

        # Working with Toolbars
        tool_bar = ToolBarMain(status_bar)
        self.addToolBar(tool_bar)

        # Set Central Widget
        self.setCentralWidget(central_widget)





