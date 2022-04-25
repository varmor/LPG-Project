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
        print(name, phone, lpgid, type)
        # mycursor = db.cursor()
        # mycursor.execute("INSERT INTO lpg (name, phone, lpgid, type) VALUES (%s, %s, %s, %s)", (name, phone, lpgid, type))
        # db.commit()
        # myresult = [name, phone, lpgid, type]
        return render_template('acknowledgement.html', name=name, phone=phone, lpgid=lpgid, type=type)
  
    return render_template("index.html" )

# @app.route("/acknowledgement/<int:lpgid>")
# def delete(lpgid):  
#     mycursor = db.cursor()
#     mycursor.execute("SELECT * FROM lpg WHERE lpgid = %s ", (lpgid,))
#     myresult = mycursor.fetchall()
#     return render_template('acknowledgement.html', myresult=myresult)

if __name__ == '__main__':
    app.run(debug=True)