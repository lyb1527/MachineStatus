import MySQLdb
from flask import Flask, render_template, request
app = Flask(__name__)


db = MySQLdb.connect(host='localhost', user='root', passwd='l1admin',db='HCTS')

cursor = db.cursor()



@app.route('/')
def list():

	cursor.execute("select * from combined")
	rows = cursor.fetchall()

	#cursor.execute('select * from Machine_Usage')
	#records = cursor.fetchall()
	#print(records)

	return render_template('machines.html', rows = rows)

@app.route('/')

def reserved():

	cursor.execute('select * from Machine_Usage')
	records = cursor.fetchall()
	
	






@app.route('/',methods = ['POST', 'GET'])
def addrecord():
	if request.method == 'POST':
			 
		try:
			
			tester = request.form['tester']
			duration = request.form['duration']
			#print(duration)
			usage = request.form['usage']
			note = request.form['note']		
			machine = request.form['machine']
		
			#cursor.execute("INSERT INTO combined (tester, duration, purpose, note) VALUES ('%s', '%s', '%s', '%s')" % (tester, duration, usage, note))


			cursor.execute("update combined set tester='%s', duration='%s', purpose='%s', note='%s'  where Hostname = '%s'" % (tester, duration, usage, note, machine))
			
			db.commit()
			msg = 'Machine Registered Successfully '
		except: 
			db.rollback()
			msg = "Registration failed"

		finally:
			return render_template("aftermath.html",msg = msg)
			db.close()

'''
@app.route('/')
def listrecords():

	cursor.execute("select * from Machine_Usage")
    records  = cursor.fetchall()
    return render_template('result.html', records = records)
    
'''






if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0')
   reserved()
