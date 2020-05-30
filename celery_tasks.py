import random
from time import sleep

from flask_mail import Message

from app import app, celery, mail


@celery.task
def send_async_email(email_data):
    msg = Message(
        email_data['subject'],
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[email_data['to']],
    )
    msg.body = email_data['body']
    with app.app_context():
        mail.send(msg)


@celery.task(bind=True)
def long_task(self):
    """Background task that runs a long function with progress reports."""
    verb = ('Starting up', 'Booting', 'Repairing', 'Loading', 'Checking')
    adjective = ('master', 'radiant', 'silent', 'harmonic', 'fast')
    noun = ('solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit')
    message = ''
    total = random.randint(10, 50)
    for step in range(total):
        if not message or random.random() < 0.25:
            message = f'{random.choice(verb)} {random.choice(adjective)} {random.choice(noun)}...'
        self.update_state(
            state='PROGRESS',
            meta={
                'current': step,
                'total': total,
                'status': message,
            },
        )
        sleep(1)
    return {
        'current': 100,
        'total': 100,
        'status': 'Task completed!',
        'result': 42,
    }
