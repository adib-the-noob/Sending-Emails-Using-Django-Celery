from celery.decorators import task

@task(name="send_review_email_task")