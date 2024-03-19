import os
import unittest
from pathlib import Path
from dotenv import load_dotenv
from infra.infra_api.api_wrapper import APIWrapper
from logic.api_logic.skills import Skills


class TestSkills(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.url = self.my_api.url
        env_path = Path(__file__).resolve().parent.parent.parent / '.env'
        load_dotenv(dotenv_path=env_path)
        self.token = os.getenv('SECRET_TOKEN')
        self.skills = Skills(self.my_api, self.url, self.token)
        print(self.token)
    def test_get_response_skills(self):
        self.skills.get_skills()
        print(self.skills.result)