# Epidemic Paint WebCanvas

Running on : http://webcanva.herokuapp.com

## Instructions
Install the requirements
`pip install -r requirements.txt`

Source the local environment
`source venv/bin/activate`

Run
`python manage.py runserver`

Deploys to Heroku automatically after pushing to *master*. Migrations need to be staged. 
To run the migrations on Heroku: `heroku run python manage.py migrate`
