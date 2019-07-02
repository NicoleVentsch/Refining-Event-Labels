from flask import Flask, send_file

import os

from refiningEventLabels.core.apiPage import APIPage

class FilePage(APIPage):

    def execute(self, request):
        filePath = super(FilePage, self).execute(request)
        return send_file(filePath, attachment_filename="test.xes")