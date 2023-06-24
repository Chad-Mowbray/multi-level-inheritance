import unittest
from jobs import *

class JobsTests(unittest.TestCase):
    
    def test_job_exists(self):
        job = Job()
        self.assertIsInstance(job, Job)

    def test_tech_job_is_job(self):
        tech = TechJob("customer service")
        self.assertIsInstance(tech, Job)

    def test_fe_developer(self):
        fe = FrontEndDeveloper("domain", "python")
        self.assertIsInstance(fe, Job)
        self.assertIsInstance(fe, TechJob)

    def test_manager(self):
        """Tests that Manager inherits from Job"""
        m = Manager("sales")
        self.assertIsInstance(m, Job)

    def test_scrum_master(self):
        sm = ScrumMaster("sales", "agile")
        self.assertIsInstance(sm, Job)
        self.assertIsInstance(sm, Manager)

    def test_lead_engineer(self):
        le = LeadEngineerAtStartup(1,2,3,4)
        self.assertIsInstance(le, Job)
        self.assertIsInstance(le, TechJob)
        self.assertIsInstance(le, Manager)
        self.assertIsInstance(le, FrontEndDeveloper)
        self.assertIsInstance(le, ScrumMaster)


if __name__ == "__main__":
    unittest.main()