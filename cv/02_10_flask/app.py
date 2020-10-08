from flask import Flask,redirect,url_for,request,render_template

app=Flask(__name__)


@app.route('/my')
def home():
    return render_template('login.html',title='home')
@app.route('/success/<name>')
def success(name):
    return 'welcome hello %s'%name
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['user']
        return redirect(url_for('success',name=user))
    else:
        user=request.args.get('user')
        return redirect(url_for('success',name=user))

if __name__=='__main__':
    app.run(debug=True)





