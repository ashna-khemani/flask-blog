from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['thename']  # Name given to input in index.html/line9
        if name == "Leo":
            return specialLeo(name);
        return render_template('greeting.html', name=name) # return "WASSUP %s"% name
    return render_template('index.html')

@app.route("/leologin", methods=['GET', 'POST'])
def specialLeo(usr):
    return "HOMAIGOD IS %s" % usr


if __name__ == '__main__':
    app.run(debug=True)