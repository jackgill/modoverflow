from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from modoverflow.database import Base


class Question(Base):
    __tablename__ = 'Questions'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    submitter_id = Column(String, ForeignKey('Users.id'))
    votes = Column(Integer)

    submitter = relationship("User", backref=backref('Questions', order_by=id))
    
    def __repr__(self):
        return '<Question %s>' % (self.title)
