class AdminContactDetails:

    def __init__(self, city, mobile):
        self.street1 = ""
        self.street2 = ""
        self.city = city
        self.province = ""
        self.countryCode = "IL"
        self.zipCod = ""
        self.homeTelephone = ""
        self.workTelephone = "112-898-7612"
        self.mobile = mobile
        self.workEmail = "paul1@osohrm.com"
        self.otherEmail = ""

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value


    def to_dict(self):
        return {
            "street1": "",
            "street2": "",
            "city": self.city,
            "province": "",
            "countryCode": "IL",
            "zipCode": "",
            "homeTelephone": "",
            "workTelephone": "112-898-7612",
            "mobile": self.mobile,
            "workEmail": "paul1@osohrm.com",
            "otherEmail": ""
        }



