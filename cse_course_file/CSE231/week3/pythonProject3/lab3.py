class Course(object):
    def __init__(self, name, department, course_number):
        self.name = name
        self.department = department
        self.course_number = course_number

    def __str__(self):
        return f"{self.department} {self.course_number} is \"{self.name}\""


class ElectiveCourse(Course):
    def __init__(self, name, department, course_number, concentration):
        super().__init__(name, department, course_number)
        self.concentration = concentration

    def __str__(self):
        return super().__str__() + f" and focuses on {self.concentration}"


class RequiredCourse(Course):
    def __init__(self, name, department, course_number):
        super().__init__(name, department, course_number)

    def __str__(self):
        return super().__str__() + " and is a core requirement"


course_list = [
    ElectiveCourse("Introduction to Machine Learning", "CSE", 404, "machine learning"),
    RequiredCourse("Introduction to Programming I", "CSE", 231),
    ElectiveCourse("Film Directing", "FLM", 335, "film production"),
    Course("Organic Chemistry I", "CEM", 251)
]


print(isinstance(course_list[0], ElectiveCourse))