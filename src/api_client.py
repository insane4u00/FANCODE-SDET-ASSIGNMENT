import requests
import logging
from pprint import pformat

# Configure logging to log to both console and file
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
file_handler = logging.FileHandler('run.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class ApiClient:
    """
    A client to interact with the JSONPlaceholder API.
    """
    BASE_URL = "http://jsonplaceholder.typicode.com"

    @staticmethod
    def get_users():
        """
        Fetch the list of users from the API.

        Returns:
            list: A list of users.
        """
        logging.info("Fetching users from the API")
        response = requests.get(f"{ApiClient.BASE_URL}/users")
        response.raise_for_status()
        logging.debug(f"Users response: {pformat(response.json())}")
        logging.info("Users fetched successfully")
        return response.json()

    @staticmethod
    def get_todos():
        """
        Fetch the list of todos from the API.

        Returns:
            list: A list of todos.
        """
        logging.info("Fetching todos from the API")
        response = requests.get(f"{ApiClient.BASE_URL}/todos")
        response.raise_for_status()
        logging.debug(f"Todos response: {pformat(response.json())}")
        logging.info("Todos fetched successfully")
        return response.json()
