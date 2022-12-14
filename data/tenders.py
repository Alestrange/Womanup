import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Tender(SqlAlchemyBase):
    __tablename__ = 'tenders_table'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    short_description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    exp_date = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    weights = sqlalchemy.Column(sqlalchemy.String, nullable=True)