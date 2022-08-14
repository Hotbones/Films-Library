# Films-Library
A local movies library project written in django

A small project in where I try my resolution of the 12th chapter's excercise of the python's course on Open-Bootcamp.

For this, I use the MDN tutorial home page, as well as some files from their github repository.

# Excercise Statement
In this excercise you will have to build an application in Django that stores data of film directors and then their's movies, as well as a description of them.

You have to customize the admin of the app and create the views of each of the parts of the app.

# Quick Start (guide taken from the mdn's repository)
To get this project up and running locally on your computer:

  1 - Set up the Python development environment. We recommend using a Python virtual environment.
      Note: This has been tested against Django 3.1.2 (and may not work or be "optimal" for other versions).

  2 - Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python to start Python):
        *  pip3 install -r requirements.txt
        *  python manage.py makemigrations
        *  python manage.py migrate
        *  python manage.py collectstatic
        *  python manage.py test # Run the standard tests. These should all pass.
        *  python manage.py createsuperuser # Create a superuser
        *  python manage.py runserver
          
  3 - Open a browser to http://127.0.0.1:8000/admin/ to open the admin site
  4 - Create a few test objects of each type.
  5 - Open tab to http://127.0.0.1:8000 to see the main site, with your new objects.
