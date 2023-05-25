from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['thename']  # Name given to input in index.html/line9
        return render_template('greeting.html', name=name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)