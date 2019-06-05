from flask import Flask, render_template
from abc import ABC, abstractmethod

import os

from refiningEventLabels.core.apiPage import APIPage

class TemplatePage(APIPage):

    def execute(self, request):
        templatePath = super(TemplatePage, self).execute(request)
        parentTemplateDir = os.path.abspath(templatePath)
        templateName = os.path.basename(templatePath)
        app = Flask(__name__, static_folder='frontend')
        return render_template(templateName)