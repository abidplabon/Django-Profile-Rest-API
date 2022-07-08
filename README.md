for connecting with the server we need command
    -vagrant up (for installation)
To Start the server 
    -vagrant ssh
Move to vagrant
    - cd /vagrant

Virtual Environment
    python -m venv ~/env
    source ~env/bin/activate
requirements.txt(to install them)
    -pip install -r requirements.txt
Admin Project Creation
    -django-admin.py startproject profiles_project .
For API Creation
    -python manage.py startapp profiles_api

Make / Add package names in the settings.py file

python manage.py runserver 0.0.0.0:8000



For model 
    -model class create and add attribute
    -make a manager to handle the model and init it inside using objects=""
    -def function to make sure the overriden attributes are not taken for granted
    -make init function to make the total thing a meaning full outcome

For API
    -Make a class with the name of the API
    -API generally asks for a function so make a function and       return something from that
For API Call
    -make a urls.py file and add the newly added urls.py as reference to the original file
    -Then work as in with the given url file patterns
PUT,PATCH,DELETE
    -Make a serializer with self and serializer class
    -go to the view file and create function based on the applications
        -function will request to the API through parameters
        -serializer var from class to request data
        -Valid==>get data with validation and serial class==>message==>return the message
        -Invalid return error&status
        

