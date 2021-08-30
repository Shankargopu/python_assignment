class Mammals:
    def __init__(self):
       self.members = ['Tiger', 'Elephant', 'Wild Cat']
    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            
           print('\t%s ' % member)
class Birds:
    def __init__(self):
            self.members = ['Sparrow', 'Robin', 'Duck']
    def printMembers(self):
            print('Printing members of the Birds class')
            
            for member in self.members:
               
               print('\t%s ' % member)
class Amphibians:
    def __init__(self):
        self.members=['fish','tortoise','snake']
    def printMembers(self):
        print("printing members of the Amphibians class")
        for member in self.members:
            
            print('\t%s ' % member)
        
