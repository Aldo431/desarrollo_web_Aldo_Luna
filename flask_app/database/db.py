from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, BigInteger, String, ForeignKey, DateTime, TIMESTAMP, func, extract
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload 
import pymysql 
import json

def date_time_now():
    return datetime.now()

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
    fecha_ingreso = Column(DateTime, nullable=False, default=date_time_now)
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
    comentarios = relationship("Comentario", back_populates="aviso")
    
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

class Comentario(Base):
    __tablename__ = "comentario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(80), nullable=False)
    texto = Column(String(300), nullable=False)
    fecha = Column(TIMESTAMP, nullable=False, default=datetime.now)
    aviso_id = Column(Integer, ForeignKey("aviso_adopcion.id"), nullable=False)

    aviso = relationship("AvisoAdopcion", back_populates="comentarios")

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

def get_region_by_id(region_id):
    session = SessionLocal()
    region = session.query(Region).filter_by(id=region_id).first()
    session.close()
    return region


def get_comuna_by_id(comuna_id):
    session = SessionLocal()
    comuna = session.query(Comuna).filter_by(id=comuna_id).first()
    session.close()
    return comuna

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

def get_all_avisos(page: int = 1, per_page: int = 5):
    session = SessionLocal()

    offset = (page - 1) * per_page

    total_avisos = session.query(AvisoAdopcion).count()

    avisos = (
        session.query(AvisoAdopcion)
        .order_by(AvisoAdopcion.fecha_ingreso.desc())
        .offset(offset)
        .limit(per_page)
        .all()
    )

    session.close()

    total_pages = (total_avisos + per_page - 1) // per_page

    return avisos, total_pages

def get_aviso_por_id(aviso_id):
    session = SessionLocal()
    aviso = session.query(AvisoAdopcion).options(joinedload(AvisoAdopcion.contactos)) .filter(AvisoAdopcion.id == aviso_id).first()
    session.close()
    return aviso

def agregar_comentario(aviso_id, nombre, texto, fecha):
    session = SessionLocal()
    comentario = Comentario(
        aviso_id=aviso_id,
        nombre=nombre,
        texto=texto,
        fecha=fecha
    )
    session.add(comentario)
    session.commit()
    session.close()

def get_avisos_por_tipo():
    session = SessionLocal()
    resultados = (
        session.query(AvisoAdopcion.tipo, func.count().label("cantidad"))
        .group_by(AvisoAdopcion.tipo)
        .all()
    )
    session.close()

    data = [{"tipo": tipo, "cantidad": cantidad} for tipo, cantidad in resultados]
    return data

def get_avisos_por_mes_y_tipo():
    session = SessionLocal()
    resultados = (
        session.query(
            extract("month", AvisoAdopcion.fecha_ingreso).label("mes"),
            AvisoAdopcion.tipo,
            func.count().label("cantidad")
        )
        .group_by("mes", AvisoAdopcion.tipo)
        .order_by("mes")
        .all()
    )
    session.close()

    conteos = {}
    for mes, tipo, cantidad in resultados:
        conteos.setdefault(mes, {})[tipo] = cantidad

    tipos = ["perro", "gato"] 
    data = []
    for m in range(1, 13):
        entrada = {"mes": m}
        for t in tipos:
            entrada[t] = conteos.get(m, {}).get(t, 0)
        data.append(entrada)

    return data

def get_avisos_por_dia():
    session = SessionLocal()
    resultados = (
        session.query(
            func.date(AvisoAdopcion.fecha_ingreso).label("fecha"),
            func.count(AvisoAdopcion.id).label("cantidad")
        )
        .group_by(func.date(AvisoAdopcion.fecha_ingreso))
        .order_by(func.date(AvisoAdopcion.fecha_ingreso))
        .all()
    )
    session.close()

    data = [{"fecha": str(fecha), "cantidad": cantidad} for fecha, cantidad in resultados]
    return data