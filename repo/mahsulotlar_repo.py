from config.session import session
from model.mahsulotlar import Mahsulotlar



class MahsulotlarRepo:

    def add(self,mah):
        session.add(mah)
        session.commit()
        return True
    def getAll(self):
        return session.query(Mahsulotlar).all()

    def getByID(self, id):
        return session.query(Mahsulotlar).filter(Mahsulotlar.id == id).first()
    def update(self, mah):
        m = self.getByID(mah.id)
        m.nom = mah.nom
        m.narxi = mah.narxi
        m.tur = mah.tur
        m.ulchovi = mah.ulchovi
        m.izoh = mah.izoh
        session.commit()

        return True
    def delete(self, mah):
        m = self.getByID(mah.id)
        session.delete(m)
        session.commit()
        return True