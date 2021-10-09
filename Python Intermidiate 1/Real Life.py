class human():
    def skills(self):
        print("Running,Writing,Thinking,Surviving")

class teacher(human):
    degree = True
    def reqs(self):
        print("If you are a teacher you have got to have a deggree")

class student(teacher):

    def career_path(self):
        
        career = input(print("If you want to be a teacher you have to get a deggree, do you have one? :"))
        if career == "yes":
            degree = True
            print("Student now becomes a teacher")
        elif career == "no":
            degree = False
            print("Student stays a student")

        job = input(print("Do you want to be a youtuber? :"))
        if job == "yes":
            print("Student is also a youtuber")

class Youtuber(student):
    def youtubers_action(self):
        print("I can code and teach")

y = Youtuber()
y.reqs()
y.career_path()
y.youtubers_action()


class Teacher2:
    def teachers_action(self):
        print("I can teach")


class Engineer:
    def Engineers_action(self):
        print("I can code")


class Youtuber2:
    def youtubers_action(self):
        print("I can code and teach")


class Person(Teacher2, Engineer, Youtuber2):
    pass


coder = Person()
coder.teachers_action()
coder.Engineers_action()
coder.youtubers_action()