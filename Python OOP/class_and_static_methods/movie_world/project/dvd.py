import datetime


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        creation_day, creation_month, creation_year = [int(x) for x in date.split(".")]
        month = datetime.date(creation_year, creation_month, creation_day).strftime('%B')
        return cls(name, id, creation_year, month, age_restriction)

    def __repr__(self):
        rented_status = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {rented_status}"

