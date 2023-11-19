from models.User import User
from dbInstance import db
from models.Blocklist import TokenBlocklist
#from _credential import server, driver, username, password
from _connection import get_conn
import os
import pyodbc
import repositories.stringOperator as stringOperator

class UserRepo:

    def __init__(self) -> None:
        pass

    def login(self, email, password):
        user = User.query.filter_by(e_mail=email, user_password=password).first()
        return user
        
    def register(self, USER_PASSWORD,FULL_NAME,LAST_NAME,E_MAIL,PHONE_NUMBER,REGISTRATION_TIME,LAST_LOGIN_TIME,USER_STATUS,USER_TYPE,COUNTRY,CITY):
        #connection_string = os.getenv("AZURE_SQL_CONNECTIONSTRING")
        #dev_connection_string = connection_string.format(drv=driver, svr=server, uid=username, pwd=password)
        #conn = pyodbc.connect(dev_connection_string)

        conn = get_conn()
        cursor = conn.cursor() 
        cursor.execute("INSERT INTO dbo.USER_PROFILE VALUES(?,?,?,?,?,?,?,?,?,?,?)", (
        USER_PASSWORD, FULL_NAME, LAST_NAME, E_MAIL, PHONE_NUMBER, REGISTRATION_TIME,
                LAST_LOGIN_TIME, USER_STATUS, USER_TYPE, COUNTRY, CITY))
        conn.commit()
        return E_MAIL

    def getPersonalInfor(self,MAIL):
        #connection_string = os.getenv("AZURE_SQL_CONNECTIONSTRING")
        #dev_connection_string = connection_string.format(drv=driver, svr=server, uid=username, pwd=password)
        #conn = pyodbc.connect(dev_connection_string)

        conn = get_conn()
        cursor = conn.cursor()
        row=cursor.execute("SELECT USERID,USER_PASSWORD,FULL_NAME,LAST_NAME,E_MAIL,PHONE_NUMBER,REGISTRATION_TIME,LAST_LOGIN_TIME,USER_STATUS,USER_TYPE,COUNTRY,CITY FROM dbo.USER_PROFILE WHERE E_MAIL=?",MAIL).fetchone()
        if(row is None):
            return {"code": 404,
            "message": "Not found"
            }
        row.USERID = row.USERID
        row.FULL_NAME = stringOperator.splitUnderscores(row.FULL_NAME)
        row.LAST_NAME = stringOperator.splitUnderscores(row.LAST_NAME)
        row.E_MAIL = stringOperator.splitUnderscores(row.E_MAIL)
        row.PHONE_NUMBER = row.PHONE_NUMBER
        row.REGISTRATION_TIME = row.REGISTRATION_TIME
        row.LAST_LOGIN_TIME = row.LAST_LOGIN_TIME
        row.USER_STATUS = stringOperator.splitUnderscores(row.USER_STATUS)
        row.USER_TYPE = stringOperator.splitUnderscores(row.USER_TYPE)
        row.COUNTRY = stringOperator.splitUnderscores(row.COUNTRY)
        row.CITY = stringOperator.splitUnderscores(row.CITY)

        ret={
            "code":200,
            "message":"success",
            "data":{
                "USERID":row.USERID,
                "FULL_NAME":row.FULL_NAME,
                "LAST_NAME": row.LAST_NAME,
                "E_MAIL": row.E_MAIL,
                "PHONE_NUMBER": row.PHONE_NUMBER,
                "REGISTRATION_TIME": row.REGISTRATION_TIME,
                "LAST_LOGIN_TIME": row.LAST_LOGIN_TIME,
                "USER_STATUS": row.USER_STATUS,
                "USER_TYPE": row.USER_TYPE,
                "COUNTRY": row.COUNTRY,
                "CITY": row.CITY,
            }
        }
        return ret
    def checkRegister(self,MAIL):
        conn = get_conn()
        cursor = conn.cursor()
        row=cursor.execute("SELECT USERID,USER_PASSWORD,FULL_NAME,LAST_NAME,E_MAIL,PHONE_NUMBER,REGISTRATION_TIME,LAST_LOGIN_TIME,USER_STATUS,USER_TYPE,COUNTRY,CITY FROM dbo.USER_PROFILE WHERE E_MAIL=?",MAIL).fetchone()
        if(row is not None):
            return {"code": 400,
            "message": "Already Exist",
            }
        return "Good"
