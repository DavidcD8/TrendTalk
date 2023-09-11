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

<https://trendtalk-010e54eb3de6.herokuapp.com>

**Automated Testing Documentation**

**Project Overview**

- **Project Name**: TrendTalk
- **Testing Scope**: Functionality, Usability, and Responsiveness
- **Testing Goals**: Ensure that the website functions as expected, is user-friendly, and responsive on different devices and screen sizes.

**Test Plan**

**Functional Testing**

Test Case 1: User Registration

**Scenario**: Verify that users can successfully register for an account.

- **Steps**:
- Navigate to the registration page.
- Fill in valid registration details.
- Click the "Register" button.
- Verify that the user is redirected to the profile page.

  **Expected Outcome**: User registration is successful.

Test Case 2: Post Creation

**Scenario**: Test the ability to create a new post.

**Steps**:

- Log in as an admin .
- Navigate to the "New Post" page.
- Fill in post details.
- Click the "Create Post" button.
- Verify that the new post appears on the post list.

**Expected Outcome**: Post creation is successful.

**Usability Testing**

Test Case 3: Navigation and User Experience

**Scenario**: Evaluate the website's navigation and user experience.

**Steps**:

- Navigate through the website as a new user.
- Assess the intuitiveness of the navigation menu.
- Evaluate the readability and layout of content.

  **Expected Outcome**: The website is user-friendly and intuitive.

**Responsiveness Testing**

Test Case 4: Mobile Device Compatibility

**Scenario**: Test the website's responsiveness on mobile devices.

**Steps**:

- Access the website on various mobile devices.
- Check for layout issues and readability.

  **Expected Outcome**: The website is responsive and displays correctly on mobile devices.

**Clicking Links in Liked and Commented Posts**

Test Case 5: Links in Liked and Commented Posts

**Scenario**: Test the functionality of clicking links in liked and commented posts.

**Steps**:

- Log in as a registered user.
- Navigate to the "Liked Posts" section.
- Click on a liked post's link.
- Verify that the post detail page opens.
- Repeat the above steps for the "Commented Posts" section.

  **Expected Outcome**: Links in liked and commented posts lead to the respective post detail pages.

**Liking a Post**

Test Case 6: Liking Posts

**Scenario**: Test the functionality of clicking the like button

**Steps**:

- **Log In**: If you haven't already, log in to your TrendTalk account.
- **Explore Posts**: Browse the posts on the TrendTalk platform to find one you'd like to like.
- Click on the post to view its details.
- Find the heart-shaped "Like" button below the post.
- Click the "Like" button to express your appreciation for the post.

  **Expected Outcome**: The like counter should increase when pressing the like button

**Commenting on a Post**

Test Case 7: Comment on posts

**Steps**:

- **Log In**: Ensure you are logged in to your TrendTalk account.
- **Find a Post**: Explore the platform and select a post you'd like to comment on.
- Click on the post to access its details.
- Scroll down to the comments section at the bottom of the post.
- You'll find a comment box where you can type your comment.
- Enter your comment and click the "Post Comment" button.

  **Expected Outcome**: The user should wait for the admin to approve the post.

**Test Results**

**Functional Testing**:

- Test Case 1: Passed
- Test Case 2: Passed
- Test Case 5: Passed
- Test Case 6: Passed
- Test Case 7: Passed

  **Usability Testing**:

- Test Case 3: Passed

  **Responsiveness Testing**:

- Test Case 4: Passed

  **Links in Liked and Commented Posts**
