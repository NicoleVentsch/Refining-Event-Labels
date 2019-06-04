from flask import Flask, render_template, request

from refiningEventLabels.frontend.startPage import StartPage

app = Flask(__name__, template_folder='frontend/template')
@app.route('/')
def startup():
    startpage = StartPage()
    return startpage.execute(request)