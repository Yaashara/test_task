from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Person(Base):
    """
    Класс отвечающий за модель данных в СУБД PostgreSQL
    """
    __tablename__ = 'persons_table'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))
    html = Column(String)


if __name__ == "__main__":
    """
    Первоначальное объявление БД с обнулением существующей
    """
    from sqlalchemy import create_engine
    from settings import DB_URI
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
