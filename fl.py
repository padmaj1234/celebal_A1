from flask import Flask,render_template
import MySQLdb
app = Flask(__name__)

connection = MySQLdb.connect(host='localhost',database='padmaj',user='root'
        )
cursor = connection.cursor()
@app.route('/')
def hello():
    cursor.execute('select d1.Pincode, sum(d2.Population) from data1 d1 inner join data2 d2 on d1.office_id = d2.office_id group by Pincode')
    data = cursor.fetchall()
    return '<html><head><title>Celebal</title></head><body><h1>'+str(data)+'</h1></body></html>'

if __name__ == '__main__':
    app.debug = True
    app.run(host = '127.0.0.1', port=8000)
