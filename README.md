# flask_blog
this tutorial: https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

# How to run stuff
Ensure flask is installed, and launch the app
## Installing Flask in a virtualenv
1. `pip3 install virtualenv`
2. Navigate to folder
3. `virutalenv .env`
4. `pip3 install flask`
5. Check flask is there: `python3 -c "import flask; print(flask.__version__)"`

## Running the application
1. `export FLASK_APP=hello`
2. `export FLASK_ENV=development`
3. `export FLASK_DEBUG=1`
4. `flask run`
5. Go to localhost `http://127.0.0.1:5000`
6. Slay
