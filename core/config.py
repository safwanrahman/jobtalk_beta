# These objects define the possible choices for multiple choice fields

class Positions(object):
    """Choices for the `position` field in the `Review` model"""
    ADMINISTRATOR = 0
    LECTURER = 1
    PHYSICIAN = 2
    PROFESSOR_ADJUNCT = 3
    PROFESSOR_ASSISTANT = 4
    PROFESSOR_ASSOCIATE = 5
    PROFESSOR_FULL = 6
    PROFESSOR_EMERITUS = 7
    POSTDOC = 8
    RESEARCH_ASSOCIATE = 9
    RESEARCH_SCIENTIST = 10
    STUDENT_DOCTORAL = 11
    STUDENT_MASTERS = 12
    STUDENT_MEDICAL_DOCTOR = 13
    TECHNICIAN = 14
    OTHER = 15

    CHOICES = (
        (ADMINISTRATOR, "Administrator"),
        (LECTURER, "Lecturer"),
        (PHYSICIAN, "Physician"),
        (PROFESSOR_ADJUNCT, "Professor-Adjunct"),
        (PROFESSOR_ASSISTANT, "Professor-Assistant"),
        (PROFESSOR_ASSOCIATE, "Professor-Associate"),
        (PROFESSOR_FULL, "Professor-Full"),
        (PROFESSOR_EMERITUS, "Professor-Emeritus"),
        (POSTDOC, "Postdoc"),
        (RESEARCH_ASSOCIATE, "Research Associate"),
        (RESEARCH_SCIENTIST, "Research Scientist"),
        (STUDENT_DOCTORAL, "Student-Doctoral"),
        (STUDENT_MASTERS, "Student-Master's"),
        (STUDENT_MEDICAL_DOCTOR, "Student-Medical Doctor"),
        (TECHNICIAN, "Technician"),
        (OTHER, "Other"),
    )


class ResearchFields(object):
    WEB = 0

    CHOICES = (
        (WEB, "Web"),
    )


class Genders(object):
    MALE = 0
    FEMALE = 1
    NON_CONFIRMING = 2
    OTHER = 3

    CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (NON_CONFIRMING, "Non-Conforming"),
        (OTHER, "Other")
    )


class Ethnicity(object):
    ASIAN = 0
    BLACK = 1

    CHOICES = (
        (ASIAN, "Asian"),
        (BLACK, "Black")
    )


class Departments(object):
    CSE = 0
    BBA = 1

    CHOICES = (
        (CSE, "CSE"),
        (BBA, "BBA")
    )
