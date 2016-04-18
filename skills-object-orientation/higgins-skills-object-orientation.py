# Part 1: Discussion
# What are the three main design advantages that object orientation can provide?
# Explain each concept.
    # It's like a smarter dictionary, wherein each key can have its own arbitrary data
        # or a unique way that it performs a function (called method for classes).
    # There is flexiblility, so some classes might contain attributes that similar
        # or parent classes have, but there can be much more specificity in subclasses.
    # They are structured, and offer an easy to diagram and conceptualize superclasses
        # and subclasses.

# 1. What is a class?
    # A class is a type of thing, that may have unique data, as compared to other
    # things to which it is similar. A cat is a type of thing, a Persian cat is
    # a type of cat.

# 2. What is an instance attribute?
    # Instance attributes are unique values that an instance of a class exhibits.
    # For example, Fido will belong to the class of dog, but their instance
    # attributes will be brown fur and the name Fido.

# 3. What is a method?
    # methods are like functions defined on a class. They allow for uniqueness
    # in the way that this type of object performs functions, or produces data.
    # A cat might be a type of pet, but only cats can purr, therefore "purr"
    # is a method that only instances of the class of cat of the class of pet
    # can perform.

# 4. What is an instance in object orientation?
    # An instance is an occurrence of a class - an object belonging to the class.
    # Fido the dog is an instance of an individual object of the class dog.

# 5. How is a class attribute different than an instance attribute?
#    Give an example of when you might use each.
    # A class attribute is a value that will be universal to all instances of
    # objects in that class. An instance attribute is a value that will be unique
    # to the individual instance of an object.
    # For example, a class attribute of cats is that they are all plotting the
    # destruction of humans. An instance attribute is that my feline friend who
    # is plotting the destruction of humans is named 'Snuggles.'


# Parts 2 through 5:
# Create your classes and class methods

# Part 2: Classes and Init Methods
# Make Python classes that could store each of the following three pieces of data.
# Define an __init__ method to allow callers of this class to provide initial
# values for each attribute.

class Student(object):
    """An instance of the class student can have a first_name, a last_name,
    and an address."""
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class QuestionMixin(object):
    """An instance of this class will have a question and a correct answer."""
    # this became a mixin because it is a lightweight class meant to provide a feature.
    # in this case, it is providing a feature to the Exam class.
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        print self.question
        answer = raw_input("What is your answer?")
        if answer == self.correct_answer:
            return True
        else:
            return False


class Exam(QuestionMixin, object):
    """Exam that takes a user's name"""
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """ Takes a question and a correct_answer as parameters,
        makes a question from those, and adds it to the exam's list of questions"""
        new_question = QuestionMixin(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        """Administers all of the exam's questions,
        returns user's score at the end"""
        score = 0
        # loop through each of the questions in the exam
        for question in self.questions:
        # for each question, call the question's ask_and_evaluate method
            if question.ask_and_evaluate() is True:
                score =+ 1

        return score

def take_test(Exam, Student):
    """Takes an exam and student as parameters, administers the exam,
    assigns the score to the student instance as a new attribute called score."""
# the left side of this statement is assigning the student incidence a score attribute.
# the right side of this statement is performing the function
    student.score = exam.administer()

# I think I goofed on this one, can you instantiate an item before you've received
# the input to instantiate?
def example():
    """creates an exam,
    adds a few questions to the exam, these should be part of the function,
    no need to prompt the user for questions
    creates a student
    administers the test for that student"""

    example_exam = Exam('example')
    example_exam.add_question('What is the color of Hackbright?', 'red')
    example_exam.add_question('Who is the mascot of Hackbright?', 'balloonicorn')
    example_exam.add_question('On what street is Hackbright?', 'sutter')

    student = Student()
    student.first_name = raw_input("What is your first name?")
    student.last_name = raw_input("What is your last name?")
    student.address = raw_input("What is your address?")
    take_test(example_exam, student)
    print "Well done, {}, your score is {}!".format(student.first_name, student.score)

example()

class Quiz(Exam):
    """Quizzes are a kind of exam that are pass/fail.
    If a user correctly answers >= half of the questions, they pass
    when you call the administer method on a quiz, itshould return
    true if you passed or False if you failed"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg

    def administer(self):
        """Administers all of the exam's questions,
        returns user's score at the end"""
        self.score = super(Exam, self).administer
        if self.score / float(len(self.questions)) >= 0.5:
            return True
        else:
            return False

