Install python environment:

Windows:

    python -m venv venv
    venv\Scripts\activate

    
Linux or MacOS:

    python3 -m venv venv
    source venv/bin/activate

Install needed packages:

    pip install -r requirements.txt



Make a migrations:

    python manage.py makemigrations;
    python manage.py migrate;
    
Run server:

    python manage.py runserver

URLs:

Registration user:

    http://127.0.0.1:8000/api/registration/

Login user:

    http://127.0.0.1:8000/api/login/

Write POST request in raw body:

For registration:

    {
        "username": "your_username",
        "email": "your_email@test.com",
        "password": "some_password",
        "confirm_password": "some_password"
    }

For authentication:

    {
        "username": "your_username",
        "password": "some_password"
    }