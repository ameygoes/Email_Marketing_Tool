import json

class Apollo_Data:
    def __init__(self, json_data):
        self.data = json_data
        self.id = json_data.get('id')
        self.first_name = json_data.get('first_name')
        self.last_name = json_data.get('last_name')
        self.linkedin_url = json_data.get('linkedin_url')
        self.title = json_data.get('title')
        self.email_status = json_data.get('email_status')
        self.country = json_data.get('country')
        self.email = json_data.get('email')
        self.headline = json_data.get('headline')
        self.organization_name = json_data.get('organization', {}).get('name')
        self.organization_website = json_data.get('organization', {}).get('website_url')


    def get_id(self):
        return self.data.get('id')
    
    def get_first_name(self):
        return self.data.get('first_name')

    def get_last_name(self):
        return self.data.get('last_name')

    def get_linkedin_url(self):
        return self.data.get('linkedin_url')

    def get_title(self):
        return self.data.get('title')

    def is_email_verified(self):
        return self.data.get('email_status') == 'verified'

    def get_country(self):
        return self.data.get('country')

    def get_email(self):
        return self.data.get('email')

    def get_headline(self):
        return self.data.get('headline')

    def get_organization_name(self):
        return self.data.get('organization', {}).get('name')

    def get_organization_website(self):
        return self.data.get('organization', {}).get('website_url')

    def __repr__(self) -> str:
        return f"{self.get_first_name()}"