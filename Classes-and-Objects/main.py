from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
       self.name = name
       self.age = age
       self.tracks = tracks
       self.score = score

    def change_name(self):
        print('I am '+ self.name)
    
    def change_age(self):
        print('I am ', self.age)
    
    def add_track(self):
        print('I am ', self.tracks)
    
    def get_score(self):
        print('I am ', self.score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
