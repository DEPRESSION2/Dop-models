from datetime import date, timedelta


class Employee:
    """
    first name for Dad
    """

    def __init__(self, name, salary, email):
    	self.name = name
    	self.salary = salary
    	self.email = email
    	# with open('emailw.txt', 'r') as f:
     #        for row in f:
     #            if self.email in row:
     #                raise ValueError("email exists")
    	# file.write(email + '\n')

    def email(self):
    	with open('emailw.txt', 'a') as f:
    		f.write(self.email)

    def work(self):
        """
        return text welcome to the office
        :return:
        """
        return '{} I come to the office!\n'.format(self.name)

    def check_salary(self):
        """
        check money adm days for salary
        :return:
        """
        now = date.today()
        month_start = date(now.year, now.month, 1)
        weekend = [5, 6]
        dayser = (now - month_start).days + 1
        day_count = 0
        for day in range(dayser):
            if (month_start + timedelta(day)).weekday() not in weekend:
                day_count += 1
        return '{} earned {} UAH for {} days.'.format(self.name, day_count * self.salary, day_count)

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __ne__(self, other):
        return self.salary != other.salary


class Recruiter(Employee):
    """
    class Recruter welcome to the work
    """

    def __init__(self, name, salary, email, hired_this_month):
        super().__init__(name, salary, email)
        self.hired_this_month = hired_this_month
        self.email = email

    def work(self):
        recruiter_work = super().work()[:-2]
        return recruiter_work + " and start codding."

    def __str__(self):
        # return "{}: {} {}".format(self.__class__.__name__, self.name)
        return 'Должность: {}, Имя: {}'.format(self.__class__.__name__, self.name)


class Programmer(Employee):
    """
    class Programmer
    """

    def __init__(self, name, salary, email, tech_stack, closed_this_month):
        super().__init__(name, salary, email)
        self.tech_stack = tech_stack
        self.closed_this_month = closed_this_month
        self.email = email

    def work(self):
        programmer_work = super().work()[:-2]
        return programmer_work + " and start hiring."

    def __str__(self):
        # return "{}: {} {}".format(self.__class__.__name__, self.name)
        return 'Должность: {}, Имя: {}'.format(self.__class__.__name__, self.name)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def __add__(self, other):
        stack = (set(self.tech_stack.split() + other.tech_stack.split()))
        return self.__class__("sup", 100, " ".join(stack))


class Candidate:
    """
    class Candidate  for programmer
    """

    def __init__(self, full_name, email, technologies):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies

    def work(self):
    	raise UnableToWorkException("I’m not hired yet, lol.")

    def __str__(self):
        pass

    def __abs__(self):
        pass


class Vacancy:
    """
    class Vacancy programer
    """

    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level

    def __str__(self):
        pass

    def __abs__(self):
        pass


class Nevens:
    """
    Additional class for parameters
    """

    def __init__(self, closed_this_month, tech_stack):
        self.closed_this_month = closed_this_month
        self.tech_stack = tech_stack

    def __str__(self):
        pass

    def __abs__(self):
        pass


class Listing:
    """
    Additional class for parameters
    """

    def __init__(self, main_skill_grade, main_skill):
        self.main_skill_grade = main_skill_grade
        self.main_skill = main_skill

    def __str__(self):
        pass

    def __abs__(self):
        pass


def alpha_p(self, other):
    """

    :param self:
    :param other:
    :return:
    """
    for i in self.tech_stack:
        if i not in other.tech_stack:
            other.tech_stack.append(i)
    return 'Alpha-programmer`s tech stack: {}.\n' \
           'Alpha-programmer closed this month: {}.' \
        .format(other.tech_stack, self.closed_this_month + other.closed_this_month)


if __name__ == "__main__":
    person1 = Programmer("Nikita", 750, "nikita@gmail.com",["Python", "Js", "Css", "Html"], 5)
    person2 = Programmer("Dima", 500,  "dima@gmail.com", ["Swift", "Js", "Java"], 7)
    person3 = Recruiter("Vlad", 300, "vlad@gmail.com", 10)
    person4 = Recruiter("Irina", 200, "Irina@gmail.com", 15)