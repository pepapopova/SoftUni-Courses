from unittest import TestCase, main

from project.hero import Hero


class HeroTests(TestCase):
    USERNAME = 'Pepa'
    LEVEL = 10
    HEALTH = 100
    DAMAGE = 75

    BATTLE_LEVEL_INCREMENT = 1
    BATTLE_HEALTH_INCREMENT = 5
    BATTLE_DAMAGE_INCREMENT = 5

    def setUp(self) -> None:
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test_if_innit_is_correct(self):
        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)

    def test_if_raises_error_when_battle_with_same_username(self):
        enemy = Hero('Pepa', 2, 100, 30)
        with self.assertRaises(Exception) as error:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test_if_raises_error_when_own_health_is_lower_than_zero(self):
        enemy = Hero('Nona', 2, 100, 30)
        self.hero.health -= 101
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_if_raises_error_when_enemy_health_is_lower_than_zero(self):
        enemy_username = 'Gabi'
        enemy = Hero(enemy_username, 2, -2, 20)
        with self.assertRaises(ValueError) as error:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy_username}. He needs to rest", str(error.exception))

    def test_returns_draw_when_both_players_die(self):
        enemy = Hero('Petya', self.LEVEL, self.HEALTH, self.DAMAGE)

        result = self.hero.battle(enemy)
        expected_health = self.HEALTH - (self.LEVEL * self.DAMAGE)

        self.assertEqual("Draw", result)
        self.assertEqual(expected_health, enemy.health)
        self.assertEqual(expected_health, self.hero.health)

    def test_returns_win_when_enemy_dies(self):
        enemy_level, enemy_health, enemy_damage = 5, 100, 10
        enemy = Hero('Petya', enemy_level, enemy_health, enemy_damage)

        result = self.hero.battle(enemy)
        self.assertEqual("You win", result)
        enemy_expected_health = enemy_health - (self.LEVEL * self.DAMAGE)
        hero_expected_health = self.HEALTH - (enemy_level * enemy_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual(enemy_expected_health, enemy.health)
        self.assertEqual(self.LEVEL + self.BATTLE_LEVEL_INCREMENT, self.hero.level)
        self.assertEqual(self.DAMAGE + self.BATTLE_DAMAGE_INCREMENT, self.hero.damage)
        self.assertEqual(hero_expected_health, self.hero.health)

    def test_returns_lose_when_hero_is_defeated(self):
        attacker_level, attacker_health, attacker_damage = 5, 100, 10
        attacker = Hero('Petya', attacker_level, attacker_health, attacker_damage)

        enemy = Hero('Tanya', self.LEVEL, self.HEALTH, self.DAMAGE)

        result = attacker.battle(enemy)
        self.assertEqual("You lose", result)
        enemy_expected_health = self.HEALTH - (attacker_damage * attacker_level) + self.BATTLE_HEALTH_INCREMENT
        attacker_expected_health = attacker_health - (self.LEVEL * self.DAMAGE)

        self.assertEqual(enemy_expected_health, enemy.health)
        self.assertEqual(self.LEVEL + self.BATTLE_LEVEL_INCREMENT, enemy.level)
        self.assertEqual(self.DAMAGE + self.BATTLE_DAMAGE_INCREMENT, enemy.damage)
        self.assertEqual(attacker_expected_health, attacker.health)

    def str_returns_proper_message(self):
        actual_result = str(self.hero)
        expected_result = f"Hero {self.USERNAME}: {self.LEVEL} lvl\n" \
               f"Health: {self.HEALTH}\n" \
               f"Damage: {self.DAMAGE}\n"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()