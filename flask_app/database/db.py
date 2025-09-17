from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, BigInteger, String, ForeignKey, DateTime # type: ignore
from sqlalchemy.orm import declarative_base, relationship, sessionmaker # type: ignore
import pymysql # type: ignore
import json

DB_NAME = "tarea2"
DB_USERNAME = "cc5002" 
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URI, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# --- Models ---

class Region(Base):
    __tablename__ = 'region'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)

    comunas = relationship("Comuna", back_populates="region", cascade="all, delete-orphan")


class Comuna(Base):
    __tablename__ = 'comuna'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    region = relationship("Region", back_populates="comunas")
    avisos = relationship("AvisoAdopcion", back_populates="comuna", cascade="all, delete-orphan")
    
class AvisoAdopcion(Base):
    __tablename__ = 'aviso_adopcion'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_ingreso = Column(DateTime, nullable=False, default=datetime.utcnow)
    comuna_id = Column(Integer, ForeignKey('comuna.id'), nullable=False)
    sector = Column(String(100))
    nombre = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(15))
    tipo = Column(String(10), nullable=False)  
    cantidad = Column(Integer, nullable=False)
    edad = Column(Integer, nullable=False)
    unidad_medida = Column(String(1), nullable=False)  
    fecha_entrega = Column(DateTime, nullable=False)  
    descripcion = Column(String(500))

    comuna = relationship("Comuna", back_populates="avisos")
    fotos = relationship("Foto", back_populates="aviso", cascade="all, delete")
    contactos = relationship("ContactarPor", back_populates="aviso", cascade="all, delete")


class Foto(Base):
    __tablename__ = 'foto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ruta_archivo = Column(String(300), nullable=False)
    nombre_archivo = Column(String(300), nullable=False)
    actividad_id = Column(Integer, ForeignKey('aviso_adopcion.id'), nullable=False)

    aviso = relationship("AvisoAdopcion", back_populates="fotos")

class ContactarPor(Base):
    __tablename__ = 'contactar_por'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20), nullable=False) 
    identificador = Column(String(150), nullable=False)
    actividad_id = Column(Integer, ForeignKey('aviso_adopcion.id'), nullable=False)

    aviso = relationship("AvisoAdopcion", back_populates="contactos")

def get_all_regiones():
    session = SessionLocal()
    regiones = session.query(Region).all()
    session.close()
    return regiones

def get_all_comunas():
    session = SessionLocal()
    comunas = session.query(Comuna).all()
    session.close()
    return comunas

def get_comunas_por_region(region_id):
    session = SessionLocal()
    comunas = session.query(Comuna).filter_by(region_id=region_id).all()
    session.close()
    return comunas	

def get_last_5_avisos():
    session = SessionLocal()
    avisos = (
        session.query(AvisoAdopcion)
        .order_by(AvisoAdopcion.fecha_ingreso.desc())
        .limit(5)
        .all()
    )
    session.close()
    return avisos