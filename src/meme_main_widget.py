import os.path
import shutil

from PySide6.QtWidgets import QWidget, QLabel, QScrollArea, QTextEdit, QPushButton
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout
from src.utils.utils import utils
from src.apis.meme_api import MemeApiController
from src.extra_widgets.popups import Popups


class MemeWidgetMain(QWidget):
    def __init__(self):
        super().__init__()

        self.scroll_area = QScrollArea()
        # scroll_area.setWidgetResizable(True)

        self.image_config = {"width": 512, "height": 512}

        # Buttons start
        self.reload_button = QPushButton("Reload Images")
        self.reload_button.clicked.connect(self.reload_images)

        self.save_to_folder_button = QPushButton("Save Memes")
        self.save_to_folder_button.clicked.connect(self.save_to_folder_button_clicked)

        self.clear_output_button = QPushButton("Clear Output")
        self.clear_output_button.clicked.connect(self.clear_output)

        self.clear_history_button = QPushButton("Clear History")
        self.clear_history_button.clicked.connect(self.clear_history)

        self.next_meme_button = QPushButton("Next Meme")
        self.next_meme_button.clicked.connect(self.next_meme)
        # Buttons end

        self.input_text_edit = QTextEdit()
        self.input_text_edit.setMaximumHeight(100)
        self.output_widget = QWidget()

        self.output_image = QLabel()

        self.output_image_label = QLabel("Image Caption")
        self.output_image_label.setFixedHeight(50)

        layout_output = QVBoxLayout()
        layout_output.addWidget(self.output_image)
        layout_output.addWidget(self.output_image_label)
        self.output_widget.setLayout(layout_output)

        # Layout
        layout_input = QVBoxLayout()
        layout_input.addWidget(self.input_text_edit)

        layout_output = QVBoxLayout()
        layout_output.addWidget(self.output_widget)

        layout_top = QHBoxLayout()
        layout_top.addWidget(self.reload_button)
        layout_top.addWidget(self.clear_output_button)
        layout_top.addWidget(self.save_to_folder_button)
        layout_top.addWidget(self.clear_history_button)
        layout_top.addWidget(self.next_meme_button)

        layout_left = QVBoxLayout()
        layout_left.addLayout(layout_input)
        layout_left.addLayout(layout_output)

        layout_right = QVBoxLayout()
        layout_right.addWidget(self.scroll_area)

        layout_left_right = QHBoxLayout()
        layout_left_right.addLayout(layout_left)
        layout_left_right.addLayout(layout_right)

        layout = QVBoxLayout()
        layout.addLayout(layout_top)
        layout.addLayout(layout_left_right)

        self.setLayout(layout)

    def clear_history(self):
        confirm = Popups.get_confirmation("Clear Memes History", "Do you want to clear memes history",
                                          "Think, then decide")

        if confirm:
            dir_path = utils.get_memes_dir()
            utils.empty_dir(dir_path)

    def save_to_folder_button_clicked(self):

        src_dir = utils.get_memes_dir()
        dst_dir = Popups.get_path_dir()

        if os.path.exists(dst_dir):
            # Copy the contents of the source directory to the destination directory
            print("Copying to "+dst_dir)
            try:
                # Copy all files in the source directory to the destination directory
                for file_name in os.listdir(src_dir):
                    src_path = os.path.join(src_dir, file_name)
                    dst_path = os.path.join(dst_dir, file_name)
                    if os.path.isfile(src_path):
                        if not os.path.exists(dst_path):
                            shutil.copy2(src_path, dst_path)
                            print(f"Copied {src_path} to {dst_path}")
                        else:
                            print(f"Skipping {src_path} because {dst_path} already exists")
            except:
                print("Error while trying to copy files")

        else:
            print("No directory selected")

    def next_meme(self):
        print("Next meme button")
        dirname = utils.get_memes_dir()

        meme_obj = MemeApiController()
        pixmap = meme_obj.get_pixmap()

        width = self.image_config["width"]
        height = self.image_config["height"]
        pixmap = pixmap.scaled(width, height)
        # pixmap.scaled(400,400,aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        self.output_image.setPixmap(pixmap)

        size = len(os.listdir(dirname))
        # filename = "image" + str(size) + ".jpg"
        filename = "image_meme_{:03d}.jpg".format(size)
        filepath = os.path.join(dirname, filename)

        pixmap.save(filepath)

    def clear_output(self):

        width = self.image_config["width"]
        height = self.image_config["height"]
        pixmap = QPixmap(width, height)
        pixmap.fill(QColor('white'))
        self.output_image.setPixmap(pixmap)

    def reload_images(self):
        print("Reloading images")

        dirname = utils.get_memes_dir()

        # Create a widget to contain the images
        container = QWidget()
        container_layout = QVBoxLayout()
        container.setLayout(container_layout)

        contents = os.listdir(dirname)
        contents.sort()
        print(contents)

        for filename in reversed(contents):
            # filename = 'img1.jpg'
            print(filename)
            filepath = os.path.join(dirname, filename)
            pixmap = QPixmap(filepath)
            local_label = QLabel(self)
            local_label.setPixmap(pixmap)
            container_layout.addWidget(local_label)

        # Set the container as the child widget of the scroll area
        self.scroll_area.setWidget(container)
