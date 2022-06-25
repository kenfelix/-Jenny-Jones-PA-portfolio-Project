"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from model.model import Base, User, Schedule, PA


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///mydb.db?check_same_thread=False", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str, first_name: str, last_name: str, \
        date_of_birth: str, custom_url: str) -> User:
        """saves the user to the database and return a user obj"""
        new_user = User(email=email, hashed_password=hashed_password, first_name=first_name, \
            last_name=last_name, date_of_birth=date_of_birth)
        new_user.pa.append(PA(custom_url=custom_url))
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        find_user_by - a method to find a user
        Arguments:
            kwargs: key word based argument
        Return:
            the first row found in the users
        """
        if kwargs is None:
            raise InvalidRequestError
        key_cols = User.__table__.columns.keys()
        for k in kwargs.keys():
            if k not in key_cols:
                raise InvalidRequestError
        rqrd_usr = self._session.query(User).filter_by(**kwargs).first()
        if rqrd_usr is None:
            raise NoResultFound
        return rqrd_usr

    def find_schedule_by(self, **kwargs) -> User:
        """
        find_user_by - a method to find a user
        Arguments:
            kwargs: key word based argument
        Return:
            the first row found in the users
        """
        if kwargs is None:
            raise InvalidRequestError
        key_cols = Schedule.__table__.columns.keys()
        for k in kwargs.keys():
            if k not in key_cols:
                raise InvalidRequestError
        rqrd_schedule = self._session.query(Schedule).filter_by(**kwargs).first()
        if rqrd_schedule is None:
            raise NoResultFound
        return rqrd_schedule

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates a user"""
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                raise ValueError

        self._session.commit()