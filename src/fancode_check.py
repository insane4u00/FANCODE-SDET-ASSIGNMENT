import logging
from .api_client import ApiClient
from pprint import pformat

# Configure logging to log to both console and file
logger = logging.getLogger()
file_handler = logging.FileHandler('run.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class FancodeChecker:
    """
    A checker to validate users and their task completion status.
    """

    def __init__(self):
        self.users = []
        self.todos = []

    def is_user_in_fancode_city(self, user):
        """
        Check if a user is in the Fancode city based on their geographical coordinates.

        Args:
            user (dict): The user data.

        Returns:
            bool: True if the user is in Fancode city, False otherwise.
        """
        lat = float(user['address']['geo']['lat'])
        lng = float(user['address']['geo']['lng'])
        result = -40 <= lat <= 5 and 5 <= lng <= 100
        logging.info(f"User {user['id']} in Fancode city: {result}")
        return result

    def get_user_completed_task_percentage(self, user_id):
        """
        Calculate the percentage of completed tasks for a given user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            float: The percentage of completed tasks.
        """
        user_todos = [todo for todo in self.todos if todo['userId'] == user_id]
        if not user_todos:
            logging.info(f"No todos found for user {user_id}")
            return 0
        completed_tasks = [todo for todo in user_todos if todo['completed']]
        percentage = (len(completed_tasks) / len(user_todos)) * 100
        logging.info(f"User {user_id} completed task percentage: {percentage}%")
        return percentage

    def check_fancode_users(self):
        """
        Check which users in the Fancode city have more than 50% of their tasks completed.

        Returns:
            dict: A dictionary with user IDs as keys and a boolean indicating if their completed tasks are more than 50%.
        """
        logging.info("Starting to check Fancode users")
        self.users = ApiClient.get_users()
        self.todos = ApiClient.get_todos()
        fancode_users = [user for user in self.users if self.is_user_in_fancode_city(user)]

        results = {}
        for user in fancode_users:
            completion_percentage = self.get_user_completed_task_percentage(user['id'])
            results[user['id']] = completion_percentage > 50
            logging.info(f"User {user['id']} completion percentage > 50%: {results[user['id']]}")

        logging.info("Finished checking Fancode users")
        return results
