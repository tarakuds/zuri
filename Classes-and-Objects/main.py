from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
       self.name = name
       self.age = age
       self.tracks = tracks
       self.score = score

# Expected methods
    def change_name(self, name):
        self.name = name
        print('My name has been changed to  '+ name)
        
    def change_age(self, age):
        print('I am ', self.age)
        
    def add_track(self, tracks):
        print('I am ', self.tracks)
        
    def get_score(self, score):
        score = 20.99
        print('I am ', self.score)
        return score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.89)

Bob.change_name(name="Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(59.5)
