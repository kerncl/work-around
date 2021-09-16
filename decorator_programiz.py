class celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fah(self):
        return (self.temperature()*1.8)+32

    #getter method
    @property
    def temperature(self):
        print('Getting Value ...')
        return self._temperature

    #setter method
    @temperature.setter
    def temperature(self, value):
        print('Setting value ...')
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    #temperature = property(get_temperature, set_temperature)

class justcounter:
    __secretcount = 0   #private variable

    def count(self):
        self.__secretcount += 1
        print(self.__secretcount)

#Setting value
human = celsius(37)
#Getting value
# 37
print(human.temperature)
#Getting value
#98.6
print(human.to_fah())


counter = justcounter()
counter.count()
counter.count()
counter._justcounter__secretcount #call private variable