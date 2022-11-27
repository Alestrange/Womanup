import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Tenders(SqlAlchemyBase):
    __tablename__ = 'tenders'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    short_description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    exp_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    weights = sqlalchemy.Column(sqlalchemy.String, nullable=True)