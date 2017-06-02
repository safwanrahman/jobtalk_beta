class Positions(object):
    GRAD_STUDENT = 0
    PROFESSOR = 1

    CHOICES = (
        (GRAD_STUDENT, "Grad Student"),
        (PROFESSOR, "Professor")
    )


class ResearchFields(object):
    WEB = 0

    CHOICES = (
        (WEB, "Web"),
    )


class Genders(object):
    MALE = 0
    FEMALE = 1

    CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female")
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