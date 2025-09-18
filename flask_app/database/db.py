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

    comuna = relationship("Comuna", back_populates="avisos",  lazy="joined")
    fotos = relationship("Foto", back_populates="aviso", cascade="all, delete", lazy="joined")
    contactos = relationship("ContactarPor", back_populates="aviso", cascade="all, delete")
    
    @property 
    def unidad_medida_texto(self): 
        return "años" if self.unidad_medida == "a" else "meses"

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

# --- Database Functions ---

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

def create_aviso(
    fecha_ingreso,
    comuna_id,
    sector,
    nombre,
    email,
    celular,
    tipo,
    cantidad,
    edad,
    unidad_medida,
    fecha_entrega,
    descripcion
):
    session = SessionLocal()
    nuevo_aviso = AvisoAdopcion(
        fecha_ingreso=fecha_ingreso,
        comuna_id=comuna_id,
        sector=sector,
        nombre=nombre,
        email=email,
        celular=celular,
        tipo=tipo,
        cantidad=cantidad,
        edad=edad,
        unidad_medida=unidad_medida,
        fecha_entrega=fecha_entrega,
        descripcion=descripcion
    )
    session.add(nuevo_aviso)
    session.commit()
    aviso_id = nuevo_aviso.id
    session.close()
    return aviso_id


def add_foto(aviso_id, ruta_archivo, nombre_archivo):
    session = SessionLocal()
    nueva_foto = Foto(
        ruta_archivo=ruta_archivo,
        nombre_archivo=nombre_archivo,
        actividad_id=aviso_id
    )
    session.add(nueva_foto)
    session.commit()
    session.close()


def add_contacto(aviso_id, nombre, identificador):
    session = SessionLocal()
    nuevo_contacto = ContactarPor(
        nombre=nombre,
        identificador=identificador,
        actividad_id=aviso_id
    )
    session.add(nuevo_contacto)
    session.commit()
    session.close()

def create_aviso_completo(
    fecha_ingreso,
    comuna_id,
    sector,
    nombre,
    email,
    celular,
    tipo,
    cantidad,
    edad,
    unidad_medida,
    fecha_entrega,
    descripcion,
    fotos=None,
    contactos=None
):
    aviso_id = create_aviso(
        fecha_ingreso,
        comuna_id,
        sector,
        nombre,
        email,
        celular,
        tipo,
        cantidad,
        edad,
        unidad_medida,
        fecha_entrega,
        descripcion
    )

    if fotos:
        for nombre_archivo in fotos:
            add_foto(aviso_id, f"uploads/{nombre_archivo}", nombre_archivo)

    if contactos:
        for c in contactos:
            add_contacto(aviso_id, c["nombre"], c["identificador"])

    return aviso_id    