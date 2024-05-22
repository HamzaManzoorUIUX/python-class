from flask import Flask, render_template,request
import psycopg2 
app = Flask(__name__)
# Connect to the database 
conn = psycopg2.connect(database="freeservice", user="postgres", 
                        password="postgres", host="localhost", port="5432") 
  # create a cursor 
cur = conn.cursor() 

@app.route('/')
def index():
    # close the cursor and connection 
    cur.execute("select name,id,email,city from users where city='lahore';")
    # Fetch the data 
    data = cur.fetchall() 
    print(data)
    return render_template('index.html',data=data)
@app.route('/', methods=['POST'])
def addData():
    name = request.form['name']
    id = request.form['id']
    email = request.form['email']
    city = request.form['city']
    password = request.form['password']
    cur.execute(f"insert into users (name,id,email,city,password) values ('{name}', '{id}', '{email}', '{city}', '{password}')")
    conn.commit()
    return "inset data successfully"
# cur.close() 
# conn.close() 

app.run(debug=True)