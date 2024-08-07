from orange_hrm.infra.utilities import Utilities
from orange_hrm.logic.api.enums.gender import Gender


class AdminObject:
    """
    This class manages admin object details.
    """

    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.employeeId = 5665
        self.otherId = 3443
        self.drivingLicenseNo = 123456789
        self.drivingLicenseExpiredDate = "2023-10-18"
        self.gender = Utilities.get_random_from_enum(Gender)
        self.maritalStatus = "Single"
        self.birthday = "2023-10-21"
        self.nationalityId = 4

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value


    def to_dict(self):
        """
        This method returns admin object details in dictionary format.
        """
        return {
            "lastName": self._last_name,
            "firstName": self._first_name,
            "middleName": self._middle_name,
            "employeeId": "5665",
            "otherId": "3443",
            "drivingLicenseNo": "123456789",
            "drivingLicenseExpiredDate": "2023-10-18",
            "gender": self.gender,
            "maritalStatus": "Single",
            "birthday": "2023-10-21",
            "nationalityId": 4
        }
