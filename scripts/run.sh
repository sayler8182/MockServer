. venv/bin/activate

export MOCK_SERVER_FLASK_HOST=127.0.0.1
export MOCK_SERVER_FLASK_PORT=5012
export MOCK_SERVER_FLASK_DATABASE_INITIALIZED=true

flask --app app --debug run --with-threads -h $MOCK_SERVER_FLASK_HOST -p $MOCK_SERVER_FLASK_PORT