import os
import unittest
from pathlib import Path
from dotenv import load_dotenv
from infra.infra_api.api_wrapper import APIWrapper
from logic.api_logic.goals import Goals


class TestGoals(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.url = self.my_api.url
        env_path = Path(__file__).resolve().parent.parent.parent / '.env'
        load_dotenv(dotenv_path=env_path)
        self.token=os.getenv('SECRET_TOKEN')
        self.goals = Goals(self.my_api, self.url,self.token)
        print(self.token)
    def test_get_response_goals(self):
        self.goals.get_goals()
        print(self.goals.result)

    def test_post_goal(self):
        self.goals.post_a_goal("Game developer",{
                "304a5801-6670-43c1-8e48-3fb45dd31f4c": {
                    "level": 50
                },
                "afa1cc12-6ecd-475c-a7f1-a130452e617e": {
                    "level": 50
                },
                "78e00084-0212-4f21-b130-481a66e92196": {
                    "level": 50
                },
                "75e13f34-a8d9-4e12-8fdf-47f4abaab487": {
                    "level": 50
                }
            }, 6)
        print(self.goals.result)

