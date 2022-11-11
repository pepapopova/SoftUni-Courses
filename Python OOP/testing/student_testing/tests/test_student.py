from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    NAME = 'Pepa'
    COURSES = {}

    def setUp(self) -> None:
        self.student = Student(self.NAME)

    def test_student_init_without_courses(self):
        self.assertEqual(self.NAME, self.student.name)
        self.assertEqual(self.COURSES, self.student.courses)

    def test_student_init_with_courses(self):
        course = {'Python Advanced': ['note 1', 'note 2']}
        student = Student(self.NAME, course)
        self.assertEqual(self.NAME, self.student.name)
        self.assertEqual(course, student.courses)

    def test_enroll_student_updates_course_notes_when_course_is_already_enrolled(self):
        course_name = 'Python Advanced'
        courses = {course_name: ['note 1', 'note 2']}
        student = Student(self.NAME, courses)
        result = student.enroll(course_name, ['note 3', 'note 4'])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['note 1', 'note 2', 'note 3', 'note 4'], student.courses[course_name])

    def test_enroll_student_extends_courses_with_course_and_notes_when_add_course_notes_is_missing(self):
        course_name = 'Python OOP'
        course_notes = ['note 1', 'note 2']

        result = self.student.enroll(course_name, course_notes)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(['note 1', 'note 2'], self.student.courses[course_name])

    def test_enroll_student_extends_courses_with_course_and_notes_when_add_course_notes_is_y(self):
        course_name = 'Python OOP'
        course_notes = ['note 1', 'note 2']

        result = self.student.enroll(course_name, course_notes, "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(['note 1', 'note 2'], self.student.courses[course_name])

    def test_enroll_student_extends_courses_with_course_and_notes_when_add_course_notes_is_invalid_and_add_notes_is_passed(self):
        course_name = 'Python OOP'
        course_notes = ['note 1', 'note 2']

        result = self.student.enroll(course_name, course_notes, "None")
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses[course_name])

    def test_raises_error_when_add_notes_passes_invalid_course(self):
        with self.assertRaises(Exception) as error:
            self.student.add_notes('Python Advanced', 'Note 3')
        self.assertEqual("Cannot add notes. Course not found.", str(error.exception))

    def test_adds_notes_updates_when_course_is_valid(self):
        course_name = 'Python advanced'
        courses = {course_name: ['note 1', 'note 2']}
        student = Student(self.NAME, courses)

        result = student.add_notes(course_name, 'note 3')
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['note 1', 'note 2', 'note 3'], student.courses[course_name])

    def test_leave_course_when_course_is_non_existent(self):
        with self.assertRaises(Exception) as error:
            self.student.leave_course('Python Advanced')
        self.assertEqual("Cannot remove course. Course not found.", str(error.exception))

    def test_leave_course_when_course_is_enrolled(self):
        self.student.enroll('Python Advanced', ['note 1'])
        result = self.student.leave_course('Python Advanced')
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)
