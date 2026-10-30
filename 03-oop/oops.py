import csv
import os


class Equipment:
    service_rate = 0.1      # class attribute (shared)
    inventory = []          # holds every object made

    def __init__(self, name: str, units: int, cost: float = 500):
        assert units >= 0, f"units can't be negative: {units}"
        assert cost >= 0, f"cost can't be negative: {cost}"

        self.__name = name      # private
        self.units = units
        self.cost = cost
        Equipment.inventory.append(self)

    @property
    def name(self):             # getter
        return self.__name

    @name.setter
    def name(self, new_name):   # setter
        self.__name = new_name

    def total_cost(self):
        return self.units * self.cost

    def yearly_service(self):
        # instance value if it's set, otherwise the class value
        return self.total_cost() * self.service_rate

    def service(self):          # abstraction: the details are in private methods
        return self.__inspect() + " / " + self.__oil()

    def __inspect(self):
        return f"checked all {self.units} {self.name}"

    def __oil(self):
        return "oiled the moving parts"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.units}, {self.cost})"

    @classmethod
    def import_csv(cls):
        csv_path = os.path.join(os.path.dirname(__file__), "item.csv")
        with open(csv_path) as f:
            for record in csv.DictReader(f):
                cls(name=record["name"], units=int(record["units"]), cost=float(record["cost"]))

    @staticmethod
    def is_int(num):            # helper, no self/cls needed
        if isinstance(num, float):
            return num.is_integer()
        return isinstance(num, int)


class Treadmill(Equipment):     # inheritance
    treadmills = []

    def __init__(self, name: str, units: int, cost: float = 500, max_speed: float = 16):
        super().__init__(name, units, cost)
        assert max_speed > 0, f"max speed has to be above 0: {max_speed}"
        self.max_speed = max_speed
        Treadmill.treadmills.append(self)


Equipment.import_csv()
print(Equipment.inventory)

stride = Treadmill("StrideMax T5", 2, 85000, 18)
print(Treadmill.treadmills, stride.total_cost())   # [...] 170000

Equipment.service_rate = 0.08    # class level, changes it for all
stride.service_rate = 0.15       # only for this object
print(stride.yearly_service(), Equipment.inventory[0].yearly_service())   # 25500.0 1920.0

print(Equipment.is_int(10.0), Equipment.is_int("10"))   # True False

bench = Equipment("Flat Bench", 4, 6500)
bench.name = "Adjustable Bench"
print(bench.name, "|", bench.service())
