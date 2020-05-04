class taxi():
    def __init__(self, unit_price, threshold_km, starting_fare):
        self.unit_price = unit_price
        self.threshold_km = threshold_km
        self.starting_fare = starting_fare

    # The main function
    def count_fare(self):
        self.record_itinerary()
        self.fare_calcultate()
        self.payment_information()

    # Store distance
    def record_itinerary(self):
        self.distance = float(input("what is the distance of this journey? "))

    # Calculate the fare
    def fare_calcultate(self):
        if self.distance <= self.threshold_km:
            self.price = self.starting_fare
        else:
            self.price = self.starting_fare + (self.distance - self.threshold_km) * self.unit_price

    # print the payment information
    def payment_information(self):
        print('The total price will be ' + str(self.price))


Mike_taxi = taxi(2.5, 3, 15)
Mike_taxi.count_fare()