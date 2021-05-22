from sqlalchemy.exc import SQLAlchemyError

from repo.mahsulotlar_repo import Mahsulotlar, MahsulotlarRepo


class MahsulotlarService:
    mr=MahsulotlarRepo()
    def add(self, mah):
        try:

            return self.mr.add(mah)
        except SQLAlchemyError as e:
            print("Mahsulot qo'shib bo'lmadi!!!")
            print(e)
            return  False
    def update(self, mah):
        try:

            return self.mr.update(mah)
        except SQLAlchemyError as e:
            print("Mahsulotni o'zgartirib bo'lmadi!!!")
            print(e)
            return  False

    def getAll(self):
        return self.mr.getAll()
    def delete(self, mr):
        try:

            return self.mr.delete(mah)

        except SQLAlchemyError as e:
            print("Mahsulotni o'chirib bo'lmadi!!!")
            print(e)
            return  False