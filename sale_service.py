from sale_repository import *

def addSale(sale):
    print(sale)
    createRecord(sale)

class SaleService:
    def __init__(self):
        self.session = Session()

    def create_user(self, name):
        user = User(name=name)
        self.session.add(user)
        self.session.commit()
        return user

    def get_user(self, user_id):
        return self.session.query(User).filter_by(id=user_id).first()

    def update_user(self, user_id, new_name):
        user = self.get_user(user_id)
        user.name = new_name
        self.session.commit()
        return user

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        self.session.delete(user)
        self.session.commit()

    def addSale(sale):
        createRecord(sale)