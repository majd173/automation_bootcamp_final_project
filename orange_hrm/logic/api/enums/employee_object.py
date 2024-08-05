class EmployeeObject:
    def __init__(self, id, firstname, middle_name, lastname):
        self.id = id
        self.firstname = firstname
        self.middle_name = middle_name
        self.lastname = lastname

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = value

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = value

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        self._lastname = value

    def to_dict(self):
        return {
                  "firstName": self.firstname,
                  "middleName": self.middle_name,
                  "lastName": self.lastname,
                  "empPicture": None,
                  "employeeId": self.id
                }
