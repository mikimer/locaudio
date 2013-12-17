
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def get_x(self):
        return self.x


    def get_y(self):
        return self.y


    def set_x(self, x):
        self.x = x
        return self


    def set_y(self, y):
        self.y = y
        return self


    def to_list(self):
        return [self.x, self.y]


    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)

