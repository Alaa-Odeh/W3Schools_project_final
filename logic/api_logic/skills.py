class Skills:

    def __init__(self,api_object,url,token):
        self.api_object = api_object
        self.new_url = url + "competency-api/skills"
        self.token = token

    def get_skills(self):
        print(self.new_url)
        self.result = self.api_object.api_get_request(self.new_url,self.token)
