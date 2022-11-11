class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans= []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.get_entity(subscription_id, self.subscriptions)
        customer = self.get_entity(subscription.customer_id, self.customers)
        trainer = self.get_entity(subscription.trainer_id, self.trainers)
        plan = self.get_entity(subscription.exercise_id, self.plans)
        equipment = self.get_entity(plan.equipment_id, self.equipment)
        return str(subscription) + '\n' + str(customer) + '\n' + str(trainer) + '\n' + str(equipment) + \
            '\n' + str(plan)

    def get_entity(self, searched_id, entity):
        for object in entity:
            if object.id == searched_id:
                return object

