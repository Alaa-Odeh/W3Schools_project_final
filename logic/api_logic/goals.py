class Goals:
    def __init__(self,api_object,url,token):
        self.api_object = api_object
        self.new_url = url+"goals-api/goals"
        self.token =token

    def get_goals(self):
        self.result = self.api_object.api_get_request(self.new_url,self.token)

    def get_goal_name_and_id_as_a_list(self):
        self.get_goals()
        self.id_name_dict = {}
        for user_id, user_info in self.result.items():
            name = user_info.get('name', '')
            self.id_name_dict[user_id] = name

        print(self.id_name_dict)




    def post_a_goal(self,name,skills,hours_per_week):
        body = {
            "name": name,
            "skills": skills,
            "hoursPerWeek": hours_per_week
        }
        self.result = self.api_object.api_post_request(self.new_url,body,self.token).json()

