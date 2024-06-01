import logging
import pytest
from src.fancode_check import FancodeChecker

# Configure logging for the test module to log to both console and file
logger = logging.getLogger()
file_handler = logging.FileHandler('run.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def test_check_fancode_users():
    """
    Test the check_fancode_users method to ensure users with more than 50% task completion are correctly identified.
    """
    logging.info("Starting test for check_fancode_users")
    checker = FancodeChecker()
    results = checker.check_fancode_users()
    for user_id, is_above_50 in results.items():
        assert is_above_50, f"User {user_id} has less than 50% tasks completed."
    logging.info("Finished test for check_fancode_users")
