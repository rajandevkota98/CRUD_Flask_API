from flask import Flask,  request, jsonify

import mysql.connector as conn


app = Flask(__name__)
mydb = conn.connect(host='localhost',user = 'root', passwd = 'password')
cursor = mydb.cursor()
cursor.execute("create database  if not exists APItester;")
cursor.execute("create table if not exists APItester.APItable(name varchar(30), number  int);")


@app.route('/insert',methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into APItester.APItable  values(%s , %s)",(name ,number))
        mydb.commit()
        return jsonify(str('Successfully inserted'))


@app.route('/get', methods = ['GET'])
def get():
    if request.method == 'GET':
        cursor.execute("select * from APItester.APItable")
        l = []
        for i in cursor.fetchall():
            l.append(i)
        return  jsonify(str(l))

@app.route("/delete" , methods= ['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        cursor.execute("delete from APItester.APItable where name = %s",(name_del,))
        mydb.commit()
        return jsonify(str("deleted successfully"))



@app.route("/update" , methods= ['POST'])
def update():
    if request.method=='POST':
         get_name = request.json['get_name']
         cursor.execute("update APItester.APItable set number = number + 500 where name = %s ",(get_name,))
         mydb.commit()
         return jsonify(str("updated successfully"))

if __name__ == '__main__':
    app.run()