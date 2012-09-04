from sqlalchemy import Column, Integer, String, Boolean
from modoverflow.database import Base
import hashlib
import string
import random

class User(Base):
    __tablename__ = 'Users'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)
    password_salt = Column(String)
    is_admin = Column(Boolean)
    
    def __repr__(self):
        return '<User %s>' % (self.email)

    def set_password(self, password_text):
        self.password_salt = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(8))
        self.password_hash = hashlib.sha512(self.password_salt + password_text).hexdigest()

    def is_valid_password(self, password_text):
        candidate_hash = hashlib.sha512(self.password_salt + password_text).hexdigest()
        return candidate_hash == self.password_hash
