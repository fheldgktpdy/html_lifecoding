from flask import Flask, render_template, request, redirect, url_for, session
import csv

app = Flask(__name__)
Id="None"
status=False
print(Id,status)

@app.route('/')
def index():
    global Id
    global status
    return render_template('index.html',inputid=Id,inputstatus=status)

@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method=='POST':
        register_info= request.form
        username=register_info['username']
        password=register_info['password']
        f=open('peoplelist.csv','a',newline='')
        mywriter=csv.writer(f)
        mywriter.writerow([username,password])
        f.close()
        
    return render_template('login1.html')

@app.route('/login1',methods=['GET','POST'])
def login1():
    global Id
    global status
    if request.method=='POST':
        login1_data=request.form
        _id=login1_data['username']
        _pw=login1_data['password']
        f=open('peoplelist.csv','r')
        data=csv.reader(f)

        for i in data:
            if i[0]==_id and i[1]==_pw:

                Id=i[0] 

                status=True
                return render_template('index.html',inputid=Id,inputstatus=status)
        if i[0]!=_id or i[1]!=_pw:
            status=False
            return render_template('index.html',inputid=Id,inputstatus=status)
    return render_template('login1.html', inputid=Id, inputstatus=status)  

@app.route('/logout',methods=['POST'])
def logout():
    global Id
    global status
    if request.method=='POST':
        status=False
    return render_template('index.html',inputid=Id,inputstatus=status)

if __name__ == '__main__':
  app.run(debug=True)
