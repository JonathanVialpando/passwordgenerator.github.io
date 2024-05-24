from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])

def home():
    if request.method == "POST":
        form = request.form.get('form')
        
        if form == "generate":
            strength = request.form.get("strength")
            if strength == "weak":
                finalPassword = generatePassword(1)
                return render_template('resultsGenerate.html', password=finalPassword)
            if strength == "medium":
                finalPassword = generatePassword(2)
                return render_template('resultsGenerate.html', password=finalPassword)
            if strength == "strong":
                finalPassword = generatePassword(3)
                return render_template('resultsGenerate.html', password=finalPassword)
    
        if form == "check":
            password = request.form.get("passwordCheck")
            finalMSG = checkPassword(password)
            return render_template('resultsCheck.html', finalMSG=finalMSG)

    return render_template('home.html')
#def chechPassword(password):
    # if password.

def generatePassword(strength):
    passwordList = string.ascii_lowercase
    if strength == 1:
        finalPassword = ''.join(random.choice(passwordList) for i in range(8))
        return finalPassword
    elif strength == 2:
        passwordList += string.ascii_uppercase
        finalPassword = ''.join(random.choice(passwordList) for i in range(10))
        return finalPassword
    elif strength == 3:
        passwordList += string.digits + string.ascii_uppercase
        finalPassword = ''.join(random.choice(passwordList) for i in range(15))
        return finalPassword

def checkPassword(password):
    msg = ""
    if password == "":
        msg += "Your password is VERY weak, try to use some characters"
        return msg
    if len(password) < 8: 
        msg += "Try adding more characters <br>"
    if password.islower() :
        msg += "Try using capital characters <br>"
    if any(char.isdigit() for char in password) == 0:
        msg += "Try using a digit <br>"
    if msg == "":
        msg += "Your password is Strong!"
    return msg 

if __name__ == '__main__':
    app.run(debug=True)
