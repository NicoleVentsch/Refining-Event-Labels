from flask import Flask
from abc import ABC, abstractmethod

class APIPage():

    def __init__(self):
        self._methods = []

    def execute(self, request):
        if request.method == "GET" and "GET" in self._methods:
            return self._GET(request)
        elif request.method == "POST" and "POST" in self._methods:
            return self._POST(request)
        elif request.method == "DELETE" and "DELETE" in self._methods:
            return self._DELETE(request)
        else:
            return self._DEFAULT(request)


    @abstractmethod
    def _GET(self, request):
        pass

    @abstractmethod
    def _POST(self, request):
        pass

    @abstractmethod
    def _DELETE(self, request):
        pass

    def _DEFAULT(self, request):
        pass #Implementation ist not required