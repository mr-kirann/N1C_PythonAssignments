# Fourth Assignment

This project is a Django-based web application for managing student-related data. Follow the steps below to set up and run the project on your local machine.

## Prerequisites
- Python 3.x installed
- Django installed (see below for installation)

## Project Structure
- `manage.py`: Django management script
- `students/`: Django app containing views, models, templates, etc.
- `db.sqlite3`: SQLite database file

## How to Run the Project

### 1. Clone or Download the Repository
Make sure you have the project files on your local machine.

### 2. Set Up a Virtual Environment (Recommended)
```
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```

### 3. Install Django
If you do not have Django installed, run:
```
pip install django
```

### 4. Apply Migrations
Run the following command to create the necessary database tables:
```
python manage.py migrate
```

### 5. Run the Development Server
Start the Django development server:
```
python manage.py runserver
```

### 6. Access the Application
Open your web browser and go to:
```
http://127.0.0.1:8000/
```

You should now see the home page of the Fourth Assignment Django application.

## Notes
- If you make changes to models, run `python manage.py makemigrations` and `python manage.py migrate` again.
- To create a superuser for the admin site, run `python manage.py createsuperuser` and follow the prompts.

## License
This project is for educational purposes.
