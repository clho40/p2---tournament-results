########## Header ##########
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
#from sqlalchemy_utils import database_exists, create_database
Base = declarative_base()
############################

########## Body ##########
class Catalog(Base):
    __tablename__ = 'catalog'
    id = Column(Integer,primary_key = True)
    name = Column(String(100),nullable=False)
    
class CatalogItem(Base):
    __tablename__ = 'catalog_item'
    id = Column(Integer,primary_key = True)
    name = Column(String(100),nullable=False)
    description = Column(String(250))
    catalog_id = Column(Integer,ForeignKey('catalog.id'))
    catalog = relationship(Catalog)
############################

########## Footer ##########
engine = create_engine('postgresql://vagrant:vagrant@localhost/catalog')
Base.metadata.create_all(engine)

# engine = create_engine("postgres://vagrant:vagrant@/postgres")
# conn = engine.connect()
# conn.execute("commit")
# conn.execute("drop database IF EXISTS catalog")
# conn.execute("commit")
# conn.execute("create database catalog")
# conn.execute("commit")
# conn.close()
############################