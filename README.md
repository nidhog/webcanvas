# Epidemic Paint WebCanvas

Running on : http://webcanva.herokuapp.com

## Instructions
### Set up the virtual environment
First install `virtualenv` using pip

`pip install virtualenv`

Then create a virtual environment for the project

`virtualenv venv`

Now you can run

`source venv/bin/activate`

### Installing the dependencies
After the virtual environment is set we can install the requirements using:

`pip install -r requirements.txt`

### Running the server locally
Then apply the migrations using:

`python manage.py migrate`

And finally Running the server using:

`python manage.py runserver`


Deploys to Heroku automatically after pushing to *master*. Migrations need to be staged. 
To run the migrations on Heroku: `heroku run python manage.py migrate`
