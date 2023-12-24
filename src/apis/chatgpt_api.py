""" Open AI Api"""

import openai
import os
from src.apis.api_key_controller import ApiKeyController
from src.localStorage.storage_query_settings import StorageQuerySettings
from src.utils import utils


class ChatGPTApiController:
    def __init__(self):
        print("API controller constructor called")
        # self.filename = "/home/darklord/Desktop/openai-client/secret_apikey.txt"

        # dirname = os.path.dirname(__file__)
        dirname = utils.get_config_dir()
        self.filename = os.path.join(dirname, 'secret_apikey.txt')
        self.api_key_controller = ApiKeyController()

    # Get response using the api
    def get_response_string(self, prompt_string):
        if len(prompt_string) < 10:
            return {"status": False, "text": "Invalid Input : Prompt is too small"}

        OPENAI_API_KEY = self.api_key_controller.get_apikey()
        if len(OPENAI_API_KEY) < 25:
            return {"status": False, "text": "Invalid API key : API key is too small"}

        # Assuming that API key is valid
        openai.api_key = OPENAI_API_KEY
        storage_query_settings = StorageQuerySettings()
        settings_dic = storage_query_settings.get_text_settings()
        print("Query Settings : ", settings_dic)
        # print(self.response.choices[0].text)

        try:
            # Make your OpenAI API request here
            response = openai.Completion.create(model=settings_dic["model"], prompt=prompt_string,
                                                temperature=settings_dic["temperature"],
                                                max_tokens=settings_dic["max_tokens"])
            output_dic = {"status": True, "text": response.choices[0].text}
        except openai.error.Timeout as e:
            # Handle timeout error, e.g. retry or log
            print(f"OpenAI API request timed out: {e}")
            output_dic = {"status": False, "text": "Error :- \n" + f"OpenAI API request timed out: {e}"}
            pass
        except openai.error.APIError as e:
            # Handle API error, e.g. retry or log
            print(f"OpenAI API returned an API Error: {e}")
            output_dic = {"status": False, "text": "Error :- \n" + f"OpenAI API returned an API Error: {e}"}
            pass
        except openai.error.APIConnectionError as e:
            # Handle connection error, e.g. check network or log
            print(f"OpenAI API request failed to connect: {e}")
            output_dic = {"status": False, "text": "Error :- \n" + f"OpenAI API request failed to connect: {e}"}
            pass
        except openai.error.InvalidRequestError as e:
            # Handle invalid request error, e.g. validate parameters or log
            print(f"OpenAI API request was invalid: {e}")
            output_dic = {"status": False, "text": "Error :- \n" + f"OpenAI API request was invalid: {e}"}
            pass
        except openai.error.AuthenticationError as e:
            # Handle authentication error, e.g. check credentials or log
            print(f"OpenAI API request was not authorized: {e}")
            output_dic = {"status": False, "text": "Error :- \n" + f"OpenAI API request was not authorized: {e}"}
            pass
        except openai.error.PermissionError as e:
            # Handle permission error, e.g. check scope or log
            print(f"OpenAI API request was not permitted: {e}")
            output_dic = {"status": False, "text": "Error :- \n" + f"OpenAI API request was not permitted: {e}"}
            pass
        except openai.error.RateLimitError as e:
            # Handle rate limit error, e.g. wait or log
            print(f"OpenAI API request exceeded rate limit: {e}")
            output_dic = {"status": False, "text": "Error :- \n" + f"OpenAI API request exceeded rate limit: {e}"}
            pass
        except ValueError as e:
            print(f"Value Error : {e}")
            output_dic = {"status": False, "text": "Error :- \n" + f"Value Error : {e}"}
            pass
        except:
            print("Inside the bare error block")
            output_dic = {"status": False, "text": "Error :- \n" + "Could not recognize type of error"}
            pass

        # return response.choices[0].text
        return output_dic

# list engines
# engines = openai.Engine.list()

# print the first engine's id
# print(engines.data[0].id)

# create a completion
# completion = openai.Completion.create(engine="ada",prompt=my_prompt)
# response = openai.Completion.create(model="text-davinci-003", prompt=my_prompt, temperature=0, max_tokens=7)
