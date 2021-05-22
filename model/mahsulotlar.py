from sqlalchemy import Column, Integer, String, ForeignKey
from model.base import Base



class Mahsulotlar(Base):
    __tablename__ ="mahsulotlar"
    id = Column(Integer, primary_key = True)
    nom = Column(String, nullable=True)
    narxi = Column(int, nullable=True)
    tur = Column(String, nullable=True)
    ulchovi = Column(int, nullable=True)
    izoh = Column(String, nullable=True)

