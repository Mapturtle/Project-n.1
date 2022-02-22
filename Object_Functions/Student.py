class Student:
    def __init__(self, name, major, gpa):
        self.name= name
        self.major= major
        self.gpa= gpa
    def on_on_honor_roll(self):             #parametr = je self cokoliv v zavorce je parametr
        if self.gpa >= 3.5:
            return True
        else:
            return False