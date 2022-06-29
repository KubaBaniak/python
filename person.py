class Person():
    
    def __init__(self, addr, client):
        self.addr = addr
        self.name = None
        self.client = client

    def set_name(self, name):
        self.name = name

    def __repr__(self):
        return 'Person {}, {}'.format(self.addr, self.name)