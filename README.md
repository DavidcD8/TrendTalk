# Table of Contents

- Overview
- Features
- Technology
- Requirements
- Getting Started
- Database
- Static Files and Media
- Security
- Configuration

# Overview

The TrendTalk Blog application is a Django-based web application that enables users to create, view, and manage blog posts. This README outlines the key components and configurations used in the application.

# Features

- Create, edit, and delete blog posts
- User authentication and registration using Django-Allauth
- Stylish frontend using Bootstrap 5 and Django-Crispy-Forms
- Cloud storage for images using Cloudinary and Dj3-Cloudinary-Storage
- Rich text editing with Django-Summernote
- PostgreSQL database for data storage

# Technologies Used

- Django 3.2.20
- Django-Allauth 0.55.0
- Django-Bootstrap5 23.3
- Django-Crispy-Forms 1.14.0
- Django-Summernote 0.8.20.0
- Gunicorn 21.2.0
- Cloudinary 1.34.0
- Dj3-Cloudinary-Storage 0.0.6
- PostgreSQL
- HTML, CSS, JavaScript

# Requirements

The application requires the following packages and libraries to be installed:

- Python 3.9 or later
- Django 3.2.20
- Django-Allauth 0.55.0
- Django-Bootstrap5 23.3
- Django-Crispy-Forms 1.14.0
- Django-Summernote 0.8.20.0
- Gunicorn 21.2.0
- Cloudinary 1.34.0
- Dj3-Cloudinary-Storage 0.0.6
- PostgreSQL database
- Pillow 10.0.0
- Psycopg2 2.9.7
- PyJWT 2.8.0
- Python3-OpenID 3.2.0
- OAuthLib 3.2.2
- Pytz 2023.3
- Requests-OAuthLib 1.3.1
- Sqlparse 0.4.4
- Urllib3 1.26.16

# Getting Started

To set up and run the TrendTalk Blog application locally, follow these steps:

- Clone the repository to your local machine.
- Make sure you have Python and pip installed.
- Create a virtual environment and activate it.
- Install the required dependencies using the following command:
- Copy code
  pip install -r requirements.txt
- Create a .env file in the project directory and define the following environment variables:
  makefile
- Copy code
  SECRET_KEY=your-secret-key
  DATABASE_URL=your-database-url
  Run the application using the following command:

- Copy code
  python manage.py runserver
- Access the application in your web browser at <http://127.0.0.1:8000/>.

# Database

The application uses a PostgreSQL database, configured using the dj_database_url package. The database URL is fetched from the DATABASE_URL environment variable.

# Static Files and Media

Static files (CSS, JavaScript, etc.) and media files are managed using Cloudinary for storage. The configuration includes settings for MEDIA_URL, DEFAULT_FILE_STORAGE, STATIC_URL, and STATICFILES_STORAGE.

# Security

The application includes security measures such as CSRF protection and password validation. Ensure that the environment variables are kept secret and the application is not run in debug mode in a production environment.

# Credits & Acknowledgments

- [Code Institute](https://codeinstitute.net/):I would like to extend my heartfelt thanks to the Code Institute for providing the project classes that were instrumental in developing the TrendTalk Blog application.
- [CI] For providing
- [Django](https://www.djangoproject.com/): The web framework used to build this application.
- [Cloudinary](https://cloudinary.com/): The cloud-based platform used for managing static files and media.
- [dj_database_url](https://pypi.org/project/dj-database-url/): A package for configuring the database using environment variables.
- [Bootstrap](https://getbootstrap.com/): The front-end framework for styling the application.
- [Python](https://www.python.org/): The programming language used to write the application's logic.
- [GitHub](https://github.com/): The platform used for version control and collaboration.
- [Youtube](https://www.youtube.com/watch?v=_P_-gum7rio): for profile Photo guidance
- [Djanog-wbesite](https://forum.djangoproject.com/t/django-how-to-connect-user-profile-model-with-comment-model-for-showing-data-from-user-profile/9134): user profile photo on comments

# Deploying TrendTalk Blog to Heroku

- Prepare Your Project

  - Ensure your project has the necessary files:
  - requirements.txt to list required Python packages.
  - Procfile to specify how Heroku should run your app.

- Set Up Version Control

  - Make sure your project is under version control using Git.
  - Initialize a Git repository if needed:bashCopy codegit init git add . git commit -m "Initial commit"

- Login to Heroku

  - If you don't have a Heroku account, sign up at Heroku.
  - Use the Heroku CLI to log in:bashCopy codeheroku login

- Create a New Heroku App

  - Create a new Heroku app with a name of your choice:bashCopy codeheroku create your-app-name

- Configure GitHub Deployment

  - Connect your Heroku app to your GitHub repository from the Heroku dashboard.
  - Enable automatic deployment from your desired branch.

- Configure Environment Variables

  - Set environment variables like SECRET_KEY, DEBUG, and others in the Heroku app settings.

- Deploy Your App

  - Trigger a manual deployment from the Heroku dashboard or let Heroku automatically deploy when changes are pushed to the connected GitHub repository.

- Configure the Database
  - Configure the database on Heroku. 
  
## Deployed website Link
https://trendtalk-010e54eb3de6.herokuapp.com
