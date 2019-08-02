from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/')
@app.route('/results', methods = ["GET", "POST"])
@app.route('/results.html', methods = ["GET", "POST"])

def results():
    score=0
    if request.method == "GET":
        return "I'm sorry, your submission is invalid."
    else:
        userdata = request.form.to_dict()
        choice1 = userdata["choice1"]
        choice2 = userdata["choice2"]
        choice3 = userdata["choice3"]
        choice4 = userdata["choice4"]
        choice5 = userdata["choice5"]
        choice6 = userdata["choice6"]
        choice7 = userdata["choice7"]
        choice8 = userdata["choice8"]
        choice9 = userdata["choice9"]
        choice10 = userdata["choice10"]


    if choice1 == "Sam and Tucker":
        score = score + 10
        c1 = "Correct, Danny's best friends are Sam and Tucker"
    else:
        score = score + 0
        c1 = "Incorrect, Danny's best friends are Sam and Tucker"

    if choice2 == "... 14":
        score = score + 10
        c2 = "Correct, Danny was just 14 years old."
    else:
        score = score + 0
        c2 = "Incorrect, Danny was just 14 years old."

    if choice3 == "Vlad Plasmius":
        score = score + 10
        c3 = "Correct, Vlad Plasmius was Danny's arch nemisis."
    else:
        score = score + 0
        c3 = "Incorrect, Vlad Plasmius was Danny's arch nemisis."

    if choice4 == "Jazz":
        score = score + 10
        c4 = "Correct, Jazz is Danny's sister."
    else:
        score = score + 0
        c4 =  "Incorrect, Jazz is Danny's sister."

    if choice5 == "He activated his parents' ghost portal.":
        score = score + 10
        c5 = "Correct, Danny got his powers when he activated his parents' ghost portal."
    else:
        score = score + 0
        c5 = "Incorrect, Danny got his powers when he activated his parents' ghost portal."

    if choice6 == "Ecto-puses":
        score = score + 10
        c6 = "Correct, Danny's first ghost fight was with Ecto-puses."
    else:
        c6 = "Incorrect, Danny's first ghost fight was with Ecto-puses."

    if choice7 == "Vlad":
        score = score + 10
        c7 = "Correct, Vlad created Danielle Fenton."
    else:
        score = score + 0
        c7 = "Incorrect, Vlad created Danielle Fenton."

    if choice8 == "My Brother's Keeper":
        score = score + 10
        c8 = "Correct, Jazz found out that Danny was half-ghost in 'My Brother's Keeper'"
    else:
        score = score + 0
        c8 = "Incorrect, Jazz found out that Danny was half-ghost in 'My Brother's Keeper'"

    if choice9 == "Goin' Ghost!":
        score = score + 10
        c9 = "Correct, Danny's catchphrase is 'Going Ghost!'"
    else:
        score = score + 0
        c9 = "Incorrect, Danny's catchphrase is 'Going Ghost!'"

    if choice10 == "Technus":
        score = score + 10
        c10 = "Correct, Technus always shouts his plans."
    else:
        score = score + 0
        c10 = "Incorrect, Technus always shouts his plans."
        
    
    if score == 100:
        message = "WOW! You really know your stuff!"
    elif score == 90:
        message = "So close, but you still did amazing."
    elif score == 80:
        message = "Great job!"
    elif score == 70:
        message = "Not too great there, bud."
    elif score == 60:
        message = "Maybe you should rewatch."
    elif score == 50:
        message = "For shame"
    elif score == 40 or score == 30 or score == 20 or score == 10 or score == 0:
        messafe = "Why are you taking this?"
        


    return render_template("/results.html", choice1 = choice1,  choice2 = choice2,choice3 = choice3, choice4 = choice4, choice5 = choice5, choice6 = choice6, choice7 = choice7, choice8 = choice8, choice9 = choice9, chocice10 = choice10, c1 = c1, c2 = c2, c3 = c3,c4 = c4,c5 =c5, c6 = c6, c7 = c7, c8 = c8, c9 = c9,c10 = c10, score = score, message = message)


