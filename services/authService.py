from flask import jsonify, request
from flask_jwt_extended import create_access_token
from repositories.userRepo import UserRepo
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from datetime import datetime, timezone, timedelta
import time
import json
import jwtTool

userRepo = UserRepo()

def login():
        
        email = request.json['email']
        password = request.json['user_password']

        user = userRepo.login(email, password)
        if user:
            access_token = create_access_token(identity=email)
            return jsonify(message="Login succeeded!", access_token=access_token)
        else:
            return jsonify(message="Bad email or password"), 401

def register():
    print(f'***{request.json['E_MAIL']=}\n')
    data = request.get_json()
    print(f'***{data=}\n')
    USER_PASSWORD = data['USER_PASSWORD']
    FULL_NAME = data['FULL_NAME']
    LAST_NAME = data['LAST_NAME']
    E_MAIL = data['E_MAIL']
    PHONE_NUMBER = data['PHONE_NUMBER']
    COUNTRY = data['COUNTRY']
    CITY = data['CITY']
    USER_STATUS = 'ONLINE'
    USER_TYPE = 'REGULAR_USER'
    REGISTRATION_TIME = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    LAST_LOGIN_TIME = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f'***{USER_PASSWORD=}\n')
        
    result=userRepo.checkRegister(E_MAIL)
    print('***{result=}\n')
    if result!='Good':
        return result

    E_MAIL=userRepo.register(USER_PASSWORD, FULL_NAME, LAST_NAME, E_MAIL, PHONE_NUMBER, REGISTRATION_TIME,
                LAST_LOGIN_TIME, USER_STATUS, USER_TYPE, COUNTRY, CITY)

    print('***After creation {E_MAIL=}\n')
    if E_MAIL:
        access_token = create_access_token(identity=E_MAIL)
        return jsonify(message="Register succeeded!", access_token=access_token)
    else:
        return jsonify(message="Bad email or password"), 401

def errorReturn(code,message):
    ret={
            "code":code,
            "message":message,
            "data":{
            }
        }
    return ret

def getPersonalInfor():
    argsJson = request.data.decode('utf-8')
    argsJson = json.loads(argsJson)
    token=argsJson['token']
    data,expired,state,message=jwtTool.decodeToken(token)
    if(state==False):
        if(str(message)=="Signature has expired"):
            return errorReturn(401,str(message))
        return errorReturn(300,str(message))
    if expired==True:
        return errorReturn(401,"This user already expired")

    result=userRepo.getPersonalInfor(data['sub'])
    if result['code']==200:
        return result
    else:
        return errorReturn(404,"Not found")
