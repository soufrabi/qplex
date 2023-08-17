import os.path
import shutil

from PySide6.QtWidgets import QWidget, QLabel, QScrollArea, QTextEdit, QPushButton, QMessageBox
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout

from src.extra_widgets.popups import Popups
from src.globals.utils import utils
from src.apis.dalle_api import DALLEApiController


class ImageWidgetMain(QWidget):
    def __init__(self):
        super().__init__()

        self.scroll_area = QScrollArea()
        # scroll_area.setWidgetResizable(True)

        self.image_config = {"width": 512, "height": 512}
        self.api_controller = DALLEApiController()

        # Buttons start
        self.reload_button = QPushButton("Reload Images")
        self.reload_button.clicked.connect(self.reload_images)

        self.save_to_folder_button = QPushButton("Save Images")
        self.save_to_folder_button.clicked.connect(self.save_to_folder_button_clicked)

        self.clear_output_button = QPushButton("Clear Output")
        self.clear_output_button.clicked.connect(self.clear_output)

        self.clear_history_button = QPushButton("Clear History")
        self.clear_history_button.clicked.connect(self.clear_history)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_button_clicked)

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
        layout_top.addWidget(self.submit_button)

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

    def submit_button_clicked(self):
        print("Submit button clicked")

        print("Submit button clicked")
        message = QMessageBox()
        message.setMinimumSize(700, 300)
        message.setWindowTitle("Submit Confirmation")

        message.setText("Do you want to submit this query")
        message.setInformativeText("Click on Ok only if you have verified your query")
        # message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Cancel)

        # Show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose Ok")
            self.query_submit()
        elif ret == QMessageBox.Cancel:
            print("User chose Cancel")
        else:
            print("User chose unknown button")

    def query_submit(self):
        dirname = utils.get_dalle_dir()

        prompt_string = self.input_text_edit.toPlainText()
        prompt_obj = {"prompt": prompt_string}
        output_dic = self.api_controller.get_response(prompt_obj)

        if output_dic["status"]:
            print("Response Success")
            # If the response status is failure the Print the Error message
            pixmap = output_dic["pixmap"]
            message = output_dic["message"]
            self.output_image.setPixmap(pixmap)
            self.output_image_label.setText(message)

            size = len(os.listdir(dirname))
            # filename = "image" + str(size) + ".jpg"
            filename = "image_dalle_{:03d}.jpg".format(size)
            filepath = os.path.join(dirname, filename)

            pixmap.save(filepath)
        else:
            print("Response Failure")
            pixmap = QPixmap()
            message = output_dic["message"]
            self.output_image.setPixmap(pixmap)
            self.output_image_label.setText(message)


    def save_to_folder_button_clicked(self):

        src_dir = utils.get_dalle_dir()
        dst_dir = Popups.get_path_dir()

        if os.path.exists(dst_dir):
            # Copy the contents of the source directory to the destination directory
            print("Copying to " + dst_dir)
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
    def clear_history(self):
        confirm = Popups.get_confirmation("Clear Memes History", "Do you want to clear memes history",
                                          "Think, then decide")

        if confirm:
            dir_path = utils.get_dalle_dir()
            utils.empty_dir(dir_path)

    def clear_output(self):

        width = self.image_config["width"]
        height = self.image_config["height"]
        pixmap = QPixmap(width, height)
        pixmap.fill(QColor('white'))
        self.output_image.setPixmap(pixmap)

    def reload_images(self):
        print("Reloading images")

        dirname = utils.get_dalle_dir()

        # Create a widget to contain the images
        container = QWidget()
        container_layout = QVBoxLayout()
        container.setLayout(container_layout)

        contents = os.listdir(dirname)
        contents.sort()
        print(contents)

        for filename in contents:
            # filename = 'img1.jpg'
            print(filename)
            filepath = os.path.join(dirname, filename)
            pixmap = QPixmap(filepath)
            local_label = QLabel(self)
            local_label.setPixmap(pixmap)
            container_layout.addWidget(local_label)

        # Set the container as the child widget of the scroll area
        self.scroll_area.setWidget(container)
