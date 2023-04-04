import os
from naas_drivers import linkedin

class LinkedinConnect():

    def __init__(self) -> None:
        self.LI_AT =  os.environ.get("LINKEDIN_LI_AT")
        self.JSESSIONID = os.environ.get("LINKEDIN_JSESSIONID")

    def connectToLinkedin(self):
        return linkedin.connect(self.LI_AT, self.JSESSIONID)
