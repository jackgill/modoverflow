from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from modoverflow.database import Base


class Answer(Base):
    __tablename__ = 'Answers'
    
    id = Column(Integer, primary_key=True)
    text = Column(String)
    submitter_id = Column(String, ForeignKey('Users.id'))
    question_id = Column(String, ForeignKey('Questions.id'))
    votes = Column(Integer)
    is_accepted = Column(Boolean)
    
    submitter = relationship("User", backref=backref('answers', order_by=id))
    question = relationship("Question", backref=backref('answers', order_by=votes.desc()))
    
    def __repr__(self):
        return '<Answer %s>' % (self.id)
