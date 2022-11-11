class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__find_customer_by_id(customer_id)
        dvd = self.__find_dvd_by_id(dvd_id)

        # if customer is None or dvd is None:
        #     return
        if customer in self.customers and dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        # if dvd not in self.dvds:
        if dvd.is_rented:
            return "DVD is already rented"
        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            for rented_dvd in customer.rented_dvds:
                if rented_dvd.id == dvd_id and customer.id == customer_id:
                    customer.rented_dvds.remove(rented_dvd)
                    rented_dvd.is_rented = False
                    return f"{customer.name} has successfully returned {rented_dvd.name}"
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        return '\n'.join([repr(x) for x in self.customers]) + '\n' + '\n'.join([repr(x) for x in self.dvds])

    def __find_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def __find_dvd_by_id(self, dvd_id):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd
