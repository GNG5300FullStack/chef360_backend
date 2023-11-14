# Importing the necessary modules and libraries
from flask import Flask
from routes.general import general_bp
from routes.auth import auth_bp
from routes.preference import preference_bp
from _credential import server, driver, username, password
from _connection import get_connection_string
import os
from dotenv import load_dotenv
from dbInstance import db
from JWTInstance import jwt


app = Flask(__name__)  # Creating the app

app.config['JWT_SECRET_KEY'] = 'chef360'
load_dotenv()
#connection_string = os.getenv("AZURE_SQL_CONNECTIONSTRING")
connection_string = get_connection_string()
dev_connection_string = connection_string.format(drv = driver, svr = server, uid = username, pwd = password)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect={}'.format(dev_connection_string)

db.init_app(app)
jwt.init_app(app)

app.register_blueprint(general_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(preference_bp,url_prefix='/preference')



if __name__ == '__main__':  # Running the app
    app.run()