from project.student_report_card import StudentReportCard
from unittest import TestCase


class TestStudentReportCard(TestCase):
    STUDENT_NAME = 'Pepa'
    SCHOOL_YEAR = 3

    def setUp(self) -> None:
        self.student = StudentReportCard(self.STUDENT_NAME, self.SCHOOL_YEAR)

    def test_innit_works_properly(self):
        self.assertEqual(self.STUDENT_NAME, self.student.student_name)
        self.assertEqual(self.SCHOOL_YEAR, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_setter_raises_error_when_name_is_empty_string(self):
        with self.assertRaises(ValueError) as error:
            self.student.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(error.exception))
        self.assertEqual(self.STUDENT_NAME, self.student.student_name)

    def test_setter_raises_error_when_school_year_is_above_limit(self):
        with self.assertRaises(ValueError) as error:
            self.student.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))
        self.assertEqual(self.SCHOOL_YEAR, self.student.school_year)

    def test_setter_raises_error_when_school_year_is_below_limit(self):
        with self.assertRaises(ValueError) as error:
            self.student.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))
        self.assertEqual(self.SCHOOL_YEAR, self.student.school_year)

    def test_when_school_year_is_on_limit(self):
        self.student.school_year = 1
        self.assertEqual(1, self.student.school_year)

    def test_when_school_year_is_on_upper_limit(self):
        self.student.school_year = 12
        self.assertEqual(12, self.student.school_year)

    def test_setter_raises_error_when_school_year_is_negative(self):
        with self.assertRaises(ValueError) as error:
            self.student.school_year = -5
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))
        self.assertEqual(self.SCHOOL_YEAR, self.student.school_year)

    def test_add_grade(self):
        self.student.add_grade('Math', 6)
        self.assertEqual({'Math': [6]}, self.student.grades_by_subject)
        self.assertEqual([6], self.student.grades_by_subject['Math'])
        self.assertTrue('Math' in self.student.grades_by_subject)

    def test_add_grade_when_subject_is_already_in_grades_list(self):
        self.student.grades_by_subject= {'Math': [5, 6]}
        self.student.add_grade('Math', 6)
        self.assertEqual({'Math': [5, 6, 6]}, self.student.grades_by_subject)
        self.assertEqual([5, 6, 6], self.student.grades_by_subject['Math'])
        self.assertEqual(3, len(self.student.grades_by_subject['Math']))
        self.assertTrue('Math' in self.student.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.student.grades_by_subject = {'Math': [6, 5], 'English': [4, 5]}
        result = self.student.average_grade_by_subject()
        expected_result = f"Math: 5.50\n" \
                          f"English: 4.50"
        self.assertEqual(expected_result, result)

    def test_average_grade_for_all_subjects(self):
        self.student.grades_by_subject = {'Math': [6, 5], 'English': [4, 5]}
        result = self.student.average_grade_for_all_subjects()
        expected_result = f"Average Grade: 5.00"
        self.assertEqual(expected_result, result)

    def test_repr(self):
        self.student.grades_by_subject = {'Math': [6, 5], 'English': [4, 5]}
        result = repr(self.student)
        average_grade_by_subject = self.student.average_grade_by_subject()
        expected_result = f"Name: {self.STUDENT_NAME}\n" \
                 f"Year: {self.SCHOOL_YEAR}\n" \
                 f"----------\n" \
                 f"{average_grade_by_subject}\n" \
                 f"----------\n" \
                 f"Average Grade: 5.00"
        self.assertEqual(expected_result, result)