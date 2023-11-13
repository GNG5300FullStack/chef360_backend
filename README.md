# chef360_backend

* This is a build branch. We will add code to this branch and will eventually use this branch to deploy our app.

**Fork from this branch to add any changes!**

## Development environment
	In powershell:
	- Navigate into the project directory
		cd 
	- Connect to Azure sql to confirm that you can see the dev db (use your @uottawa account in Azure)

	- Create python environment and activate it:
				py -m venv .venv
				.venv\scripts\activate
	- Install requirements:
				pip install -r requirements.txt 

	- Create a your env file 
				cp .env.example .env
	- When you develop localy, remember to rename this environment variable to 'dev':
				FLASK_ENV='dev'
				
	- Create a your credential file 
				cp _credential.template.py _credential.py

	- For local development, update your _credential.py file with your SQL servername, username and password to access the db. This is not your @uottawa account!!
		(DO NOT SHARE THE CREDENTIAL OR PUSH IT TO SOURCE CONTROL)		
	- For production deployment, a user managed identity "Chef360..." was created and used in Azure App service.

	- The db connection string is already defined in .env file
	
	- Run:
		flask run			
	- To debug run:
		flask --app app.py --debug run
				


