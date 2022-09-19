. venv/bin/activate

rm app/config/app.db
rm -rf migrations

pip3 install -r requirements.txt
flask db init
flask db migrate
flask db upgrade