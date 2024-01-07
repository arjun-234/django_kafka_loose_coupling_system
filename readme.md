# Django Kafka Loose Coupling System

This project demonstrates a loosely-coupled system for user registration, welcome email sending, and logging using Django and Kafka.

## Features

- **User Registration**
- **Welcome Email Sending**
- **Logging**

## Technologies

- Django
- Kafka

## Project Structure

- **user_registration_service**
- **email_sending_service**
- **logging_service**
- **kafka_integration**

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/django_kafka_loose_coupling_system.git

2. **Install dependencies:**
    ```
    pip install -r requirements.txt

3. **Configure Django and Kafka settings:**

   - **Django Settings:**
     - Open `django_kafka_loose_coupling_system/settings.py`.
     - Configure the necessary settings for the database, Django secret key, and other relevant configurations. Additionally, provide SMTP email credentials if you intend to enable email sending functionality.
   - **Kafka Settings:**
     - If you don't have Kafka installed locally, you can use an online Kafka service or configure the services to run without Kafka.
     - If you have Kafka, provide Kafka connection details in `myapp/kafka_producer.py` and `myapp/kafka_consumer.py`.

   **Note:** If Kafka isn't installed on your local machine, you can launch Docker services by executing the command `docker-compose up -d` in the project directory. This starts Kafka services in detached mode, enabling background operation. If you prefer viewing logs directly in your terminal, omit the `-d` option when using the command `docker-compose up`.

4. **Run the Django project:**
   ```bash
   python manage.py runserver

Access the application at the server ```localhost:8000```.

5. **Run the Kafka Consumer for Registration Logs:**
Access user registration logs in the shell using the following command:

    python myapp/kafka_consumer.py

## Contributing
Feel free to contribute by opening issues or creating pull requests. Your feedback and contributions are welcome!