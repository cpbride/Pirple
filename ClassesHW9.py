class Vehicle:
    def __init__(self, Make, Model, Year, Weight, NeedsMaintenance, TripsSinceMaintenance):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0
#why is NeedsMaintenance and TripsSinceMaintenance not connecting?
    #getters
    def getMake(self):
        return self.make

    def getModel(self):
        return self.Model

    def getYear(self):
        return self.Year

    def getWeight(self):
        return self.Weight

    def NeedsMaintenance(self):
        return self.NeedsMaintenance

    def TripsSinceMaintenance(self):
        return self.trips

    #setters
    def setMake(self, Make):
        self.Make = Make

    def setModel(self, Model):
        self.Model = Model

    def setYear(self, Year):
        self.Year = Year

    def setWeight(self, Weight):
        self.Weight = Weight

    def setNeedsMaintenance(self, NeedsMaintenance):
        self.NeedsMaintenance = False

    def setTripsSinceMaintenance(self, TripsSinceMaintenance):
        self.TripsSinceMaintenance = TripsSinceMaintenance

class Cars(Vehicle):
    def __init__(self, Make, Model, Year, Weight, Drive, Stop):
        Vehicle.__init__(self, Make, Model, Year, Weight, NeedsMaintenance, TripsSinceMaintenance)
        self.Drive = Drive
        self.Stop = Stop

    def isDriving(self):
        if self.trips == True:
            return set



Cars.Drive = True

Car1 = Cars("Ford", "Mustang", "1972", "3500lbs", True, 1)

print(Car1.getYear())
print(Car1.isDriving())
