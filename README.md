Using Celery with Flask
=======================

The application provides two examples of background tasks using Celery:

- sends emails asynchronously.
- launches one or more asynchronous jobs and shows progress updates in the web page.


Quick Setup
-----------

1. Clone this repository.
2. Create a virtualenv and install the requirements.
3. Open a second terminal window and start a local Redis server (if you are on Linux or Mac, execute `run-redis.sh` to install and launch a private copy).
4. Open a third terminal window. Set two environment variables `MAIL_USERNAME` and `MAIL_PASSWORD` to a valid Gmail account credentials (these will be used to send test emails). Then start a Celery worker: `celery worker -A app.celery --loglevel=info`.
5. Start the Flask application on your original terminal window: `python app.py`.
6. Go to `http://localhost:5000/` and enjoy this application!
