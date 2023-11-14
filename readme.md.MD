What you must do for run the project?

1)Install python environment(use terminal for that):
    python -m venv venv; - Windows.
    venv\Scripts\activate - Windows.
    python3 -m venv venv; - Linux or MacOS.
    source venv/bin/activate. - Linux
    
2)Install needed packages:

pip install django;
pip install djangorestframework;
pip install djangorestframework-simplejwt;
pip install requests;
pip install django-cors-headers;
pip install djangorestframework-jwt;

3)Create a database:
    use the IDE interface - click RMB and choose you foundament directory -> that choose "New" -> File -> write: db.sqlite3

4)make a migrations for database:
    python manage.py makemigrations;
    python manage.py migrate;
    
5)After you can try to run server:
    python manage.py runserver

6)If you want use UserRegistration you need use Postman for that(not Django built-in UI),
because this code have validating for "confirming password" and built-in Django UI don't have this field in default.

7)Using Postman:
    1: Go to postman.com or download it on you PC. 
    2: Open Postman and go to page of requesting.
    3: Choose POST request in UI of Postman and write http://127.0.0.1:8000/api/registration/ in header-field.
    4: Go to "Headers" and after write: 
        Content-Type - in "Key"
        application/json - in "Value".
    5: Go to "Body" and choose the "raw"
    6: Write your request for a server:

For example:

{
  "username": "john_doe2",
  "email": "john.doe2@google.com",
  "password": "strong123",
  "confirm_password": "strong123"
}
