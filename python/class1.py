class country:
    AVG_POPULATION=24000
    
    def __init__(self,country_name,country_code):
        self.country_name=country_name
        self.country_code=country_code
        while True:
    try:
      if(country_name!=str):
          raise ValueError(country_name)
          print("only strings are allowed")
      elif(country_code!=str):
          raise ValueError(country_code)
      elif(len(country_code)!=3):
         raise ValueError(country_code)
      else:
          self.country_name=country_name
          self.country_code=country_code
    except ValueError as e:
        print(e)
          

                        
    def country_short_form(self,country_name):
        self.country_name=country_name
        return self.country_name[0:2].upper()
    def is_densly_populated(self,population):
        self.population=population
        if(self.population > AVG_POPULATION):
            return True
sum_num=0       
def world_avg_population(self,population):
    self.population=population
    for elements in the population:
    sum_num=sum_num+elements
    avg=(sum_num)/len(self.population)

ob=country(2,5)
