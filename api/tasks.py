from celery import shared_task

@shared_task
def send_welcome_email(email: str) -> str:
    # In real use: integrate Django email backend
    return f"Sent welcome email to {email}"
