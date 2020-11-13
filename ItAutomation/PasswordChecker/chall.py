from secretPassword import  SECRET_PASSWORD
from flask import Flask , request
import re 
from flask import render_template

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def index():
    if request.method== "GET":
        return render_template('index.html', title='Main')
    elif request.method == 'POST':
        # get data 
        pattern_to_check = request.form.get("regexCheck")
        if ('*' in pattern_to_check ) or ('(' in pattern_to_check ) or (')' in pattern_to_check):
            data = {
                    'type':'danger',
                    'message':'You cant use this caractere'
                }
            return render_template('index.html', title='Main', data=data)
        try:
            if re.match(pattern_to_check, SECRET_PASSWORD):
                data = {
                    'type':'success',
                    'message':'The Regex match with the password'
                }
                return render_template('index.html', title='Main', data=data)
            else:
                data = {
                    'type':'danger',
                    'message':"The Regex dont match with the password"
                }
                return render_template('index.html', title='Main', data=data)
        except Exception:
            data = {
                    'type':'danger',
                    'message':"An error happened while processing your regex"
                }
            return render_template('index.html', title='Main', data=data)
