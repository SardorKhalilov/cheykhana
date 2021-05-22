from sqlalchemy.exc import SQLAlchemyError

from repo.mahsulot_tur_repo import MahsulotTur, MahsulotTurRepo


class MahsulotTurService:
    mur=MahsulotTurRepo()
    def add(self, mt):
        try:

            return self.mur.add(mt)
        except SQLAlchemyError as e:
            print("Mahsulot turi qo'shib bo'lmadi!!!")
            print(e)
            return  False
    def update(self, mt):
        try:

            return self.mur.update(mt)
        except SQLAlchemyError as e:
            print("Mahsulot turini o'zgartirib bo'lmadi!!!")
            print(e)
            return  False

    def getAll(self):
        return self.mtr.getAll()
    def delete(self, mt):
        try:

            return self.mur.delete(mt)

        except SQLAlchemyError as e:
            print("Mahsulot turini o'chirib bo'lmadi!!!")
            print(e)
            return  False