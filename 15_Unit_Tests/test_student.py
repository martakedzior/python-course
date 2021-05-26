import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.obj_anna = Student('anna', 'kowalska', 4.0, None)
        self.obj_arek = Student('arkadiusz', 'nowak', 3.8, None)


    def test_email(self):
        print('email')
        self.assertEqual(self.obj_anna.email, 'anna.kowalska@university.com')
        self.obj_anna.name = 'joanna'
        self.assertEqual(self.obj_anna.email, 'joanna.kowalska@university.com')

    def test_fullname(self):
        print('fullname')
        self.assertEqual(self.obj_anna.fullname, 'Anna Kowalska')
        self.obj_anna.last = 'Zamezna'
        self.assertEqual(self.obj_anna.fullname, 'Anna Zamezna')

    def test_grant_scholarship(self):
        print('scholarship')
        self.obj_anna.grant_scholarship()
        self.assertEqual(self.obj_anna.scholarship, True)

        self.obj_arek.grant_scholarship()
        self.assertEqual(self.obj_arek.scholarship, False)

    def test_not_grant_scholarship(self):
        self.obj_anna.scholarship = 1.0
        self.obj_anna.grant_scholarship()
        self.assertEqual(self.obj_anna.scholarship, True)


    def tearDown(self):
        del self.obj_anna
        del self.obj_arek

if __name__ == '__main__':
    unittest.main()