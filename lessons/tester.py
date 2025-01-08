"""skiii"""

class ChristmasTreeFarm:
    plots: list[int] 

    def __init__(self, plots: int, initial_planting: int) -> None:
        self.plots = []

        i: int = 0
        while i < initial_planting:
            self.plots.append(1)
            i += 1
        
        while i < plots:
            self.plots.append(0)
            i += 1

    def plant(self, plot_index: int):
      
            self.plots[plot_index] = 1
    
    def growth(self):
        
        for i in range(len(self.plots)):
             if self.plots[i] > 0:
                  self.plots[i] += 1
    
    def harvest(self, replant: bool) -> int:
        trees_harvested: int = 0
        for i in range(len(self.plots)):
              if self.plots[i] >= 5:
                   trees_harvested += 1
                   if replant == True:
                        self.plots[i] = 1
                   else:
                        self.plots[i] = 0

                    
        return trees_harvested
    
class Car:
    make: str
    model: str
    year: int
    color: str
    mileage: float

    def __init__(self, init_make, init_model, init_year, init_color, init_mileage) -> None:
        self.make = init_make
        self.model = init_model
        self.year = init_year
        self.color = init_color
        self.mileage = init_mileage
    def update_mileage(self, miles: float):
         self.mileage += miles

    def display_info(self):
         print(f"Color: {self.color}\nMake: {self.make}\nModel:{self.model}\n Year: {self.year}\n Mileage: {self.mileage}")


def calculate_depreciation(Honda: Car, depreciation_rate: float):
     return(Honda.mileage * depreciation_rate)



class Course:
     """Models the idea of a UNC course."""
     name: str
     level: int
     prerequisites: list[str]

     def is_valid_course(self, prerequisite: str) -> bool:
          is_valid: bool = False
          if self.level >= 400 and prerequisite in self.prerequisites:
               is_valid = True
          return is_valid

my_ride: Car = Car("Honda", "CRV", "2015", "blue", 75000.00)
my_ride.update_mileage(5000.25)
my_ride.display_info()
calculate_depreciation(my_ride, .01)

def find_courses(course_list: list[Course], prerequisite: str) -> list[str]:
     good_courses: list[str] = []
     for i in course_list:
          if i.level > 400:
               if prerequisite in i.prerequisites:
                    good_courses.append(i.name)
     return good_courses
               
