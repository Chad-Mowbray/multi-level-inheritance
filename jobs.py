
class Job:
    def __init__(self):
        self.salary = 0

    def get_paid(self):
        self.salary += 1

class TechJob(Job):
    def __init__(self, domain):
        Job.__init__(self)
        self.domain = domain

    def get_paid(self):
        super().get_paid()
        self.salary += 100

class FrontEndDeveloper(TechJob):
    def __init__(self, domain, language):
        TechJob.__init__(self, domain)
        self.language = language

    def get_paid(self):
        self.salary += 1000
        # super().get_paid()
        # # Job.get_paid(self)

    def write_code(self):
        print(f"writing code in {self.language}")

class Manager(Job):
    def __init__(self, department):
        Job.__init__(self)
        self.department = department

    def manage(self):
        print("I'm Mr. Manager!")

class ScrumMaster(Manager):
    def __init__(self, department, certification):
        Manager.__init__(self, department)
        self.certification = certification

    def get_paid(self):
        super().get_paid()
        self.salary += 10000

class LeadEngineerAtStartup(FrontEndDeveloper, ScrumMaster):
    def __init__(self, domain, language, department, certification):
        FrontEndDeveloper.__init__(self, domain, language)
        ScrumMaster.__init__(self, department, certification)

