from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, address=None, home=None,
                 mobile=None, work=None, fax=None,
                 email=None, email2=None, email3=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id

    def __repr__(self):
        return "%s, lastname %s, firstname %s" % (self.id, self.lastname, self.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and (self.firstname is None or other.firstname is None or self.firstname == other.firstname)

