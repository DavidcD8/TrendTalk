# Table of Contents

- Overview
- Features
- Getting Started
- Database
- Static Files and Media
- Security
- Configuration

# Overview

The TrendTalk Blog application is a Django-based web application that enables users to create, view, and manage blog posts. This README outlines the key components and configurations used in the application.

# Features

- Create, edit, and delete blog posts.
- View a list of all blog posts on the home page.
- Read individual blog posts in detail.

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
- Access the application in your web browser at http://127.0.0.1:8000/.

# Database

The application uses a PostgreSQL database, configured using the dj_database_url package. The database URL is fetched from the DATABASE_URL environment variable.

# Static Files and Media

Static files (CSS, JavaScript, etc.) and media files are managed using Cloudinary for storage. The configuration includes settings for MEDIA_URL, DEFAULT_FILE_STORAGE, STATIC_URL, and STATICFILES_STORAGE.

# Security

The application includes security measures such as CSRF protection and password validation. Ensure that the environment variables are kept secret and the application is not run in debug mode in a production environment.
