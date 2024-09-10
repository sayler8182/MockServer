pip3 install virtualenv --break-system-packages
python3 -m venv venv

. venv/bin/activate

pip3 install -r requirements.txt --break-system-packages
flask db init
flask db migrate
flask db upgrade