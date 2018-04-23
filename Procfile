web: gunicorn channex.wsgi:application --log-file -
web2: daphne channex.asgi:application --port $PORT --bind 0.0.0.0 -v2
