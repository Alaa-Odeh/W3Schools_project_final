import time
import unittest

from infra.infra_web.browser_wrapper import BrowserWrapper
from logic.api_logic.goals_api import GoalsAPI
from logic.api_logic.skills_api import SkillsAPI
from logic.web_logic.goals_web import GoalsWeb
from logic.web_logic.home_page_pathfinder import PathfinderPage
from logic.web_logic.login_page import LoginPage
from logic.web_logic.welcome_page import WelcomePage


class TestGoalsAPI(unittest.TestCase):
    def setUp(self):
        self.goals_api = GoalsAPI()
        self.skills = SkillsAPI()
        self.browser = BrowserWrapper()
        if self.browser.config["grid"]:
            self.browser.build_cap()
        else:
            self.browser.run_single_browser()
        self.driver = self.browser._driver
        self.welcome_page = WelcomePage(self.driver)
        self.welcome_page.click_log_in()
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow("friendola15@gmail.com", "AutomationTester2024")
        self.pathfinder_page = PathfinderPage(self.driver)
        self.pathfinder_page.click_on_Goals_page()
        self.goals_web = GoalsWeb(self.driver)

    def test_create_goal_api(self):
        goal_name="Backend developer"
        chosen_skills=["HTML","C#","CSS","Go"]
        courses_levels=["Professional","Beginner","Professional","Beginner"]
        hours_weekly=8
        self.goals_web.set_goal_in_web(goal_name,chosen_skills,courses_levels,hours_weekly)
        skill_names,skill_levels=self.goals_api.get_created_goal_info(chosen_skills)
        self.assertListEqual(skill_names,chosen_skills,"Skills dont match")
        self.assertListEqual(skill_levels,courses_levels,"levels Dont Match")

    def tearDown(self):
        self.goals_api.delete_goal()



