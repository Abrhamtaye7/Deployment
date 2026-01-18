from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import send_welcome_email

@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})


@api_view(["POST"])
def welcome(request):
    email = request.data.get("email")
    if not email:
        return Response({"error": "email is required"}, status=400)

    job = send_welcome_email.delay(email)
    return Response({"task_id": job.id, "status": "queued"})

# api/views.py

def notify(request):
    # your logic here
    pass