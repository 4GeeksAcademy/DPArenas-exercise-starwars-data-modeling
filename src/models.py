import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Creamos una class que será el Modelo instanciando de Base. Naming convention: PascalCase en plural
    # 1. Creamos el alias de la tabla __tablename__ . Naming convention: snake_case
    # 2. Columnas, 
    # 2.1. Clave primaria. Tipo de dato, primary_key=True
    # 2.2. Atributos del modelo. Tipo de dato(longitud), acepta datos vacíos?, es un dato único?
    # 2.3. Clave foránea. Tipo de dato, ForeignKey('alias.id')
    # 3. Relaciones. relationship(Models)
    # 4. Métodos

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    subscription_date = Column(Date)


class Profiles(Base):
    __tablename__ = 'profiles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    img_url = Column(String, nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'), unique=True)
    users = relationship(Users)


    def to_dict(self):
        return {}


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    height = Column(String)
    mass = Column(String)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)
    homeworld = Column(String)
    url = Column(String)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String, nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    climate = Column(String)
    terrain = Column(String)
    surface_water = Column(String)
    url = Column(String)


class FavoritesCharacters(Base):
    __tablename__ = 'favorites_characters'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    users = relationship(Users)
    characters = relationship(Characters)


class FavoritesPlanets(Base):
    __tablename__ = 'favorites_planets'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    characters_id = Column(Integer, ForeignKey('planets.id'))
    users = relationship(Users)
    characters = relationship(Characters)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
