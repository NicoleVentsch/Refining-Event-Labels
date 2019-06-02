from flask import Flask, request
from abc import ABC, abstractmethod

class APIPage():

    def __init__(self):
        self._methods = []

    def execute(self):
        if request.method == "GET" and "GET" in self._methods:
            return self._GET()
        elif request.method == "POST" and "POST" in self._methods:
            return self._POST()
        elif request.method == "DELETE" and "DELETE" in self._methods:
            return self._DELETE()
        else:
            return self._DEFAULT()


    @abstractmethod
    def _GET(self):
        pass

    @abstractmethod
    def _POST(self):
        pass

    @abstractmethod
    def _DELETE(self):
        pass

    def _DEFAULT(self):
        pass #Implementation ist not required