from flask import Flask, render_template, redirect, request
from mysql import connector

app = Flask(__name__)
app.config['SECRET_KEY']='supersecretKey'

db = connector.connect(
  host="localhost",
  user="root",
  password="",
  database="lpg"
)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method =="POST":
        name = request.form["Name"]
        phone = request.form["Phone"]
        lpgid = request.form["LPG ID"]
        type = request.form["Type"]
        print(type)
        # ONKAR IT's FOR YOU
        if type == "5kg":
            amount = 200
        elif type == "9kg":
            amount = 650
        elif type == "15kg":
            amount = 800
        elif type == "45kg":
            amount = 1500
        else:
            amount= 5000
        print(name, phone, lpgid, type)
        mycursor = db.cursor()
        mycursor.execute("INSERT INTO lpg (name, phone, lpgid, type, amount) VALUES (%s, %s, %s, %s, %s)", (name, phone, lpgid, type, amount))
        db.commit()
        mycursor = db.cursor()
        mycursor.execute("SELECT name, phone, lpgid, type, amount FROM lpg")
        myresult = mycursor.fetchall()
        return render_template('index.html', myresult=myresult)

    return render_template("index.html" )

@app.route("/acknowledgement/<int:lpgid>")
def delete(lpgid):  
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM lpg WHERE lpgid = %s ", (lpgid,))
    myresult = mycursor.fetchall()
    return render_template('acknowledgement.html', myresult=myresult)


if __name__ == "__main__":
    app.run(debug=True)