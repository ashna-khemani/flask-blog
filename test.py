# Attempting to fix code on tutorialspoint that doesn't seem to work...
# This doesn't work either :(
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect("/success/%s" % user)
   else:
      user = request.args.get('nm')
      return redirect("/success/%s" % user)

if __name__ == '__main__':
   app.run(debug = True)