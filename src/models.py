from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(60), nullable=False)
    last_name: Mapped[str] = mapped_column(String(60), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    
    favorites= db.relationship("Favorite", back_populates="user", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Character(db.Model):
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
        hair_color: Mapped[str] = mapped_column(String(60), nullable=False)
        eye_color:Mapped[str] = mapped_column(String(60),  nullable=False)
        gender:Mapped[str] = mapped_column(String(60), nullable=False)
        
        favorites= db.relationship("Favorite", back_populates="character")

        def serialize(self):
            return {
            "id": self.id,
            "name": self.name,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "gender": self.gender,
        }

class Planet(db.Model):
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
        terrain: Mapped[str] = mapped_column(String(60), nullable=False)
        climate:Mapped[str] = mapped_column(String(60),  nullable=False)
        population:Mapped[int] = mapped_column(Integer) 
        
        favorites= db.relationship("Favorite", back_populates="planet")

        def serialize(self):
            return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "climate": self.climate,
            "population": self.population,
        }

class Vehicle(db.Model):
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
        model: Mapped[str] = mapped_column(String(100), nullable=False)
        vehicle_class:Mapped[str] = mapped_column(String(60),  nullable=False)
        cargo_capacity:Mapped[int] = mapped_column(Integer) 
        
        favorites= db.relationship("Favorite", back_populates="vehicle")

        def serialize(self):
            return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "cargo_capacity": self.cargo_capacity,
        }

class Favorite(db.Model):
        id: Mapped[int] = mapped_column(primary_key=True)
        user_id:Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
        character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=True)
        planet_id:Mapped[int] = mapped_column(ForeignKey("planet.id"), nullable=True)
        vehicle_id:Mapped[int] = mapped_column(ForeignKey("vehicle.id"), nullable=True)
        
        user= db.relationship("User", back_populates="favorites")
        character= db.relationship("Character", back_populates="favorites")
        planet= db.relationship("Planet", back_populates="favorites")
        vehicle= db.relationship("Vehicle", back_populates="favorites")

        def serialize(self):
            return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id,
        }
