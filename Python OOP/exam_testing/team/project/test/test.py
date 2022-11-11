from project.team import Team
from unittest import TestCase

class TeamTest(TestCase):
    name = 'Lions'
    members = {'Ivanov': 33, 'Petrov': 27}

    def setUp(self) -> None:
        self.team = Team(self.name)

    def test__if_innit_gives_proper_result_when_no_members(self):
        self.assertEqual(self.name, self.team.name)
        self.assertEqual({}, self.team.members)

    def test__if_innit_gives_proper_result(self):
        self.team.members = self.members
        self.assertEqual(self.name, self.team.name)
        self.assertEqual(self.members, self.team.members)

    def test_if_name_setter_is_raising_value_when_contains_other_than_letter(self):
        name = 'Pena9|!2932'
        with self.assertRaises(ValueError) as error:
            self.team.name = name
        self.assertEqual("Team Name can contain only letters!", str(error.exception))
        self.assertEqual(self.name, self.team.name)

    def test_if_add_members_works_properly(self):
        result = self.team.add_member(pesho=13, gosho=18)
        self.assertEqual(f"Successfully added: pesho, gosho", result)
        self.assertEqual(13, self.team.members['pesho'])
        self.assertEqual(18, self.team.members['gosho'])

    def test_if_remove_member_removes_member_when_present(self):
        name = 'pesho'
        self.team.members[name] = 14
        result = self.team.remove_member(name)
        self.assertEqual(f"Member {name} removed", result)
        self.assertEqual({}, self.team.members)
        self.assertTrue(name not in self.team.members) #!!!

    def test_if_remove_member_when_member_does_not_exist(self):
        member = 'gosho'
        self.team.members['pesho'] = 12
        result = self.team.remove_member(member)
        self.assertEqual(f"Member with name {member} does not exist", result)
        self.assertEqual({'pesho': 12}, self.team.members)

    def test_if_greater_than_works_properly(self):
        self.team.members['gosho'] = 13
        self.team.members['pesho'] = 15
        another = Team('Tigers')
        another.members['galya'] = 7
        result = self.team > another
        result2 = another > self.team
        self.assertEqual(True, result)
        self.assertEqual(False, result2)

    def test_if_len_gives_proper_result(self):
        self.team.members['gosho'] = 13
        self.team.members['pesho'] = 15
        self.assertEqual(2, len(self.team))

    def test_if_add_creates_proper_new_team(self):
        self.team.members['gosho'] = 13
        self.team.members['pesho'] = 15
        another = Team('Tigers')
        another.members['galya'] = 7
        new_team = self.team + another
        self.assertEqual('LionsTigers', new_team.name)
        self.assertEqual({'gosho': 13, 'pesho': 15, 'galya' : 7}, new_team.members)

    def test_if_string_works_properly(self):
        self.team.members['gosho'] = 13
        self.team.members['pesho'] = 15
        self.team.members['galya'] = 7
        result = str(self.team)
        expected_result = f"Team name: {self.name}\n" \
                          f"Member: pesho - 15-years old\n" \
                          f"Member: gosho - 13-years old\n" \
                          f"Member: galya - 7-years old"
        self.assertEqual(expected_result, result)
