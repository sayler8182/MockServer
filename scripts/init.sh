. venv/bin/activate
pip3 install -r requirements.txt
flask db init
flask db migrate
flask db upgrade