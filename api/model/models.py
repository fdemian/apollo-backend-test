from sqlalchemy import Column, Integer, Unicode, ForeignKey, Text, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# If the user uses oauth salt and password are null.
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    avatar = Column(Text, nullable=False)
    username = Column(Unicode(50), nullable=False)
    fullname = Column(Unicode(100), nullable=True)
    email = Column(Unicode(255), nullable=False)
    signature = Column(Unicode(255), nullable=False)
    about = Column(Unicode(255), nullable=False)
    password = Column(Text, nullable=True)
    valid = Column(Boolean, nullable=False)
    failed_attempts = Column(Integer, nullable=False)
    lockout_time = Column(DateTime, nullable=True)

    # Collections
    stories = relationship("Story", backref="user")
    accounts = relationship("OAuthAccount", back_populates="user", lazy='dynamic')
    notifications = relationship("Notification")


class OAuthAccount(Base):
    __tablename__ = 'oauth_account'

    id = Column(Integer, primary_key=True, nullable=False)
    oauth_id = Column(Unicode(100), nullable=True)  # Provider provided ID.
    provider = Column(Unicode(30), nullable=False)  # facebook, github, etc...
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="accounts")


class UserActivation(Base):
    __tablename__ = 'user_activation'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    code = Column(Text, nullable=False)

    user = relationship("User")


class PasswordChange(Base):
    __tablename__ = 'password_change_requests'

    id = Column(Integer, primary_key=True, nullable=False)
    token = Column('reset_token', Text, nullable=False)
    time = Column('time', DateTime)
    user_id = Column('user_id', Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User")


class Story(Base):
    __tablename__ = 'stories'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(Unicode(100), nullable=False)
    tags = Column(Text, nullable=True)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    author = relationship("User")
    category = relationship("Category", backref="stories")
    comments = relationship("Comment", backref="story")

    def __repr__(self):
        return '<%s %s %s %s>' % (self.id, self.title, self.content, self.author)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(50), nullable=False)
    description = Column(Text, nullable=True)
    
    def __repr__(self):
        return '<%s %s>' % (self.id, self.name)


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, nullable=False)
    author = Column(Unicode(100), nullable=True)
    content = Column(Text, nullable=False)
    avatar = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    story_id = Column(Integer, ForeignKey('stories.id'))


class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    type = Column(Text, nullable=False)
    text = Column(Text, nullable=False)
    link = Column(Text, nullable=False)
    read = Column(Boolean, nullable=False)


class GlobalConfiguration(Base):
    __tablename__ = 'global_configuration'

    key = Column(Text, primary_key=True, nullable=False)
    value = Column(Text, nullable=False)

def create_from_scratch(connection_string):
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)
