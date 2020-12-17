class Course_Grade:
    def __init__(self, assignment, graded_assignment, weight, exam_weight):
        self.assignment = assignment
        self.graded_assignment = graded_assignment
        self.weight = weight
        self.exam_weight = exam_weight
        self.graded_assignment_result = [0]*self.graded_assignment
        self.assignment_result = [False]*self.assignment
        self.final_exam = 0

    def set_assignment(self, x, assignment):
        self.assignment_result[x] = assignment

    def set_assignments(self, assignments):
        self.assignment_result = assignments

    def set_graded_assignment(self, x, graded_assignment):
        self.graded_assignment_result[x] = graded_assignment

    def set_graded_assignments(self, graded_assignments):
        self.graded_assignment_result = graded_assignments

    def set_exam(self, final_exam):
        self.final_exam = final_exam

    def get_grade(self):
        if self.assignment != 0 and False in self.assignment_result:
            return 'F'

        sum_assignment = 0
        sum_weight = 0
        if self.graded_assignment != 0:
            for i in range(self.graded_assignment):
                sum_assignment += self.graded_assignment_result[i] * self.weight[i] / 100
                sum_weight += self.weight[i]
            if sum_assignment / sum_weight < 0.4:
                return 'F'
        final_grade = sum_assignment + self.final_exam * self.exam_weight / 100
        if self.final_exam / 100 < 0.4:
            return 'F'
        else:
            if 90 <= final_grade <= 100:
                return "A"
            elif 80 <= final_grade < 90:
                return "B"
            elif 60 <= final_grade < 80:
                return "C"
            elif 50 <= final_grade < 60:
                return "D"
            elif 40 <= final_grade < 50:
                return "E"
            else:
                return "F"

class ACIT4420_2020(Course_Grade):
    def __init__(self):
        Course_Grade.__init__(self, 0, 7, [5, 7, 10, 6, 7, 8, 7], 50)

class ACIT4420_2019(Course_Grade):
    def __init__(self):
        Course_Grade.__init__(self, 7, 0, [], 100)
        

a = ACIT4420_2020()
a.set_graded_assignments([70, 70, 70, 70, 70, 70, 70])
a.set_graded_assignment(2, 100)
a.set_exam(76)
print(a.get_grade())


a2 = ACIT4420_2019()
a2.set_assignments([True, True, True, True, True, True, True])
a2.set_exam(76)
print(a2.get_grade())


b = ACIT4420_2020()
b.set_graded_assignments([20, 20, 20, 20, 20, 20, 20])
b.set_graded_assignment(2, 100)
b.set_exam(84)
print(b.get_grade())


b2 = ACIT4420_2019()
a2.set_assignments([True, True, True, True, True, True, True])
a2.set_exam(84)
print(a2.get_grade())
