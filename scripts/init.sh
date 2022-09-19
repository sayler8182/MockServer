pip3 install virtualenv
python3 -m venv venv

. venv/bin/activate

pip3 install -r requirements.txt
flask db init
flask db migrate
flask db upgrade