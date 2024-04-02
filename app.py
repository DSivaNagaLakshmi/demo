from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

'''@app.route('/',methods=['GET','POST'])
def demo():
    if request.method == 'POST':
        name = request.form['name']
        branch = request.form['marks']
        marks = request.form['branch']
        place = request.form['place']
        print(name,marks,branch,place)
    return render_template('index.html')
        
@app.route('/sita/<string:a>/<string:b>',methods=['GET','POST'])
def sita(a,b):
    print(request,args)
    return f'{a},{b}'''


@app.route('/luck/')
def lucki():
    return redirect(url_for('demo1'))
@app.route('/redirected-page')
def demo1():
    return render_template('index.html')       


app.run(use_reloader=True,debug=True)
