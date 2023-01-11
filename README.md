# webapp-python-flask

# setup virtual environment for macos python3
cd webapp-python-flask
python3 -m venv flaskenv
. flaskenv/bin/activate

pip install flask
pip install flask-login
pip install flask-sqlalchemy

# activate virtual environment
. flaskenv/bin/activate

# deactivate virtual environment
deactivate

# webserver adress
http://127.0.0.1:5000