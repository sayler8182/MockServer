. venv/bin/activate

if [ -z "${MOCK_SERVER_FLASK_HOST}" ]; then
  MOCK_SERVER_FLASK_HOST=127.0.0.1;
fi
if [ -z "${MOCK_SERVER_FLASK_PORT}" ]; then
  MOCK_SERVER_FLASK_PORT=5012;
fi

export MOCK_SERVER_AUTO_IMPORT=$1
export MOCK_SERVER_FLASK_DATABASE_INITIALIZED=true

flask --app app --debug run --with-threads -h $MOCK_SERVER_FLASK_HOST -p $MOCK_SERVER_FLASK_PORT