from memory_profiler import memory_usage
from pympler import asizeof

class Road:

    def __init__(self,length,width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self):
        return (f'{self._length} м*{self._width} м*25 кг*5 см = {self._length *self._width *25 *5 //1000} т')




a = Road(20,5000)
print(asizeof.asizeof((a))) #328
print(a.mass_of_asphalt())

class Road:

    __slots__ = ['length','width']

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def mass_of_asphalt(self):
        return (f'{self.length} м*{self.width} м*25 кг*5 см = {self.length *self.width *25 *5 //1000} т')




a = Road(20,5000)
print(asizeof.asizeof((a))) #112
print(a.mass_of_asphalt())
