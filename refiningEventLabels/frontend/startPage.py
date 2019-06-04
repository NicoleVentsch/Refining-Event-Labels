from refiningEventLabels.core.apiPage import APIPage
from refiningEventLabels.core.templatePage import TemplatePage

import os

class StartPage(TemplatePage):

    def __init__(self):
        self._methods = ["GET"]

    def _GET(self, request):
        currentDir = os.path.dirname(__file__)
        destinationTemplate = os.path.join(currentDir, "template", "startPage.html")
        return destinationTemplate

    def _POST(self, request):
        pass
        
    
    def _DELETE(self, request):
        pass