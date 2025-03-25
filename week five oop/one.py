class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  # Encapsulation (Private Attribute)

    def get_price(self):
        """Encapsulation: Get price securely."""
        return self.__price

    def call(self, number):
        print(f"📞 Calling {number} from {self.brand} {self.model}...")

    def browse(self, website):
        print(f"🌐 Browsing {website} on {self.brand} {self.model}...")

# Inheritance: Extend Smartphone class
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, health_tracking=True):
        super().__init__(brand, model, price)
        self.health_tracking = health_tracking  # Additional feature

    def track_health(self):
        print(f"📊 Tracking health on {self.brand} {self.model} Smartwatch.")

# Creating instances
phone = Smartphone("Apple", "iPhone 15", 999)
watch = Smartwatch("Samsung", "Galaxy Watch 6", 299)

phone.call("123-456-7890")
watch.track_health()
print(f"Smartphone Price: ${phone.get_price()}")
