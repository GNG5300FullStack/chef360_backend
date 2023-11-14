from models.UserPreference import UserPreference
from dbInstance import db
from models.Blocklist import TokenBlocklist

class UserPreferenceRepo:

    def __init__(self) -> None:
        pass
    def getPreference(self,email):
        userPreference=UserPreference.query.filter_by(E_MAIL=email).first()
        return userPreference
    def addPreference(self,email,cookware,allergics):
        userPreference=UserPreference(E_MAIL=email,COOKWARE=cookware,ALLERGICS=allergics)
        db.session.add(userPreference)
        db.session.commit()
    def updatePreference(self,email,cookware,allergics):
        userPreference=UserPreference.query.filter_by(E_MAIL=email)
        userPreference.COOKWARE=cookware
        userPreference.ALLERGICS=allergics
        db.session.commit()
    def updatePreference(self,userPreference,cookware,allergics):
        print(cookware)
        print(allergics)
        userPreference.COOKWARE=cookware
        userPreference.ALLERGICS=allergics
        db.session.commit()