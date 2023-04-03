import openai

class DALLEApiController:
    def __init__(self):

        print("DALLE Api")

    def get_pixmap(self,prompt_o):
        response = openai.Image.create(
            prompt="a white siamese cat",
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']