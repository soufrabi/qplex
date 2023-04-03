import requests
from PySide6.QtGui import QPixmap, QImage

class MemeApiController:
    def __init__(self):

        print("Meme API controller")

    def get_pixmap(self):

        url = 'https://meme-api.com/gimme'
        # Make a GET request to the URL and get the image data
        response = requests.get(url)
        data = response.json()

        # Get the URL of the image from the JSON object
        image_url = data['url']
        print(image_url)

        # Make a GET request to the image URL and get the image data
        response = requests.get(image_url)
        image_data = response.content

        # print(image_data)

        # Create a QImage object from the image data
        image = QImage.fromData(image_data)

        # Create a QPixmap object from the QImage object
        pixmap = QPixmap.fromImage(image)

        # print(pixmap)
        return pixmap



