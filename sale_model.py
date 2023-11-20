class Sale:
    def __init__(self, id, name, totalCost, category, email, description, completed=False):
        id 
        self.name = name
        self.description = description
        self.totalcost = totalCost
        self.categoty = category
        self.email = email
        self.completed = completed
    
    @property
    def id(self):
        return self.id
    @id.setter
    def id(self, value):
        self.id = value

    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, value):
        self.name = value
        
    @property
    def totalCost(self):
        return self.totalCost
    @totalCost.setter
    def totalCost(self, value):
        self.totalCost = value

    @property
    def category(self):
        return self.category
    @category.setter
    def category(self, value):
        self.category = value

    @property
    def email(self):
        return self.email
    @email.setter
    def email(self, value):
        self.email = value

    @property
    def description(self):
        return self.description
    @description.setter
    def description(self, value):
        self.description = value

    @property
    def completed(self):
        return self.completed
    @completed.setter
    def completed(self, value):
        self.completed = value






    #         id = Column(Integer, primary_key=True)
    # name = Column(String)
    # totalCost = Column(Integer)
    # category = Column(String)
    # email = Column(String)
    # description = Column(String)
    # completed = Column(bool)