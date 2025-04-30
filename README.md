# Book Review API

This is a Django REST Framework API project for managing books and user reviews, with JWT-based authentication.

## Requirements

- Python 3.8+
- Django
- djangorestframework
- djangorestframework-simplejwt

## How to Run the Project Locally

1. Clone the repository (if hosted on GitHub):
   ```bash
   git clone https://github.com/Dk1x/bookreview_project.git
   cd bookreview_project
 2. Create a virtual environment:
 python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt
4. Apply migrations:
 python manage.py migrate
5. Create a superuser (for admin access):
To create a superuser (an admin user who can access the Django admin panel), run:
python manage.py createsuperuser
6. Run the development server:
python manage.py runserver
7. Open your browser and go to http://127.0.0.1:8000/ to start using the API.
8. How to test each endpoint
## How to Test Each Endpoint

Use Postman or similar tool:

- Register: POST /api/register/
- Login: POST /api/token/
- Refresh Token: POST /api/token/refresh/
- Change Password: POST /api/change-password/
- Book List: GET /api/books/
- Book Detail: GET /api/books/<id>/
- Create Book (admin): POST /api/books/
- Edit Book (admin): PUT /api/books/<id>/
- Delete Book (admin): DELETE /api/books/<id>/
- Add Review: POST /api/books/<book_id>/reviews/
- Get Reviews: GET /api/books/<book_id>/reviews/
- Edit Review: PUT /api/reviews/<id>/
- Delete Review: DELETE /api/reviews/<id>/

## Authentication

- JWT authentication using djangorestframework-simplejwt.
- Use Authorization: Bearer <access_token> in the headers for protected routes.