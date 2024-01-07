from django.core.mail import send_mail
from django.shortcuts import render
from .models import User
from .kafka_producer import produce_message
from django_kafka_loose_coupling_system.settings import EMAIL_HOST_USER

def register_user(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        # Save user to the database
        user = User(email=email, password=password)
        user.save()

        # Produce message to Kafka for logging
        message = f"User registered: {email}"
        produce_message('user_registration_logs', message)

        # Send welcome email (you can implement this part)
        # Send welcome email
        email_subject = 'Welcome to Our Website'
        email_message = f'Thank you for registering, {email}!'
        from_email = EMAIL_HOST_USER
        to_email = [user.email]
        send_mail(email_subject, email_message, from_email, to_email, fail_silently=False)

        return render(request, 'registration_success.html', {'username': email})

    return render(request, 'register.html')
