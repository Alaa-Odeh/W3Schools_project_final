import os
import unittest
from infra.infra_api.api_wrapper import APIWrapper
from logic.api_logic.goals import Goals


class TestGoals(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.url = self.my_api.url
        #self.token = self
        self.token=os.getenv('SECRET_TOKEN')
        self.goals = Goals(self.my_api, self.url,self.token)
    def test(self):
        self.goals.get_goals()
        print(self.goals.result)