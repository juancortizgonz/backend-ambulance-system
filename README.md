# Intelligent ambulance management system

## Project overview

This project is built using Django and Django Rest Framework. It provides a robust backend through a RESTful API.

## Main requirements

- Django 5.1.2
- Django Rest Framework 3.14.0
- Python 3.12
- drf-spectacular (OpenAPI 3)
- django-environ

## Features

1. Clone the repository:

    `git clone git@github.com:juancortizgonz/backend-ambulance-system.git`

    Then, using the terminal move to the new repository.

2. Create and activate a virtual environment:

    `python -m venv venv`
    
    Linux/Mac:
    
    `source venv/bin/activate`

    On Windows use:

    `.\venv\Scripts\activate`

3. Install the dependencies. Note that there are two requirements files. The one with the `dev` flag should only be used in local development environments, as it contains dependencies for tests and linters, so it should be avoided in production.:

    `pip install -r requirements.txt`

---

## Usage

1. Apply migrations:

    `python manage.py migrate`

2. Run the development server:
    
    `python manage.py runserver`

3. Access the application at `http://127.0.0.1:8000/`

4. In order to access all the endpoints you must be authenticated. This application uses token authentication. To generate the token make a `POST` request to `api/v1/auth` endpoint and save it for later use.

5. With each new request, ensure to add the `Authorization` header and add the token to it, like the following:

    `Authorization: Token <generated-token>`

6. Remember to create groups and permissions automatically using the command:
    `python manage.py create_groups`

---

## API Endpoints

You can check all the available endpoints visiting the Swagger UI in `api/v1/schema/swagger-ui/`.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.