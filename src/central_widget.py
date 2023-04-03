from PySide6.QtWidgets import QWidget,QHBoxLayout
from PySide6.QtWidgets import QTabWidget
from src.text_main_widget import TextMainWidget
from src.image_main_widget import ImageWidgetMain
from src.audio_main_widget import AudioWidgetMain
from src.meme_main_widget import MemeWidgetMain


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()

        # self.setMinimumSize(800,600)
        self.widget_text = TextMainWidget()
        self.widget_image = ImageWidgetMain()
        self.widget_audio = AudioWidgetMain()
        self.widget_memes = MemeWidgetMain()

        tab_widget = QTabWidget(self)

        tab_widget.addTab(self.widget_text,"Text")
        tab_widget.addTab(self.widget_image,"Image")
        tab_widget.addTab(self.widget_audio,"Audio")
        tab_widget.addTab(self.widget_memes, "Memes")

        layout = QHBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)


