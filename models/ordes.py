class Orders():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, styleId, metalId, sizeId):
        self.id = id
        self.styleId = styleId
        self.metalId = metalId
        self.sizeId = sizeId
       
   