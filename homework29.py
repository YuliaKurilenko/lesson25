import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.runner = Runner('Петя')
        t = 0
        for i in range(0, 10):
            t += 1
            self.runner.walk()
        dist_1 = self.runner.distance
        self.assertEqual(dist_1, 50)

    def test_run(self):
        self.runner_ = Runner('Вася')
        t = 0
        for _ in range(0, 10):
            t += 1
            self.runner_.run()
        self.assertEqual(self.runner_.distance, 100)

    def test_challenge(self):
        self.runner1 = Runner('Коля')
        self.runner2 = Runner('Леша')
        t = 0
        for _ in range(0, 10):
            t += 1
            self.runner1.run()
            self.runner2.walk()
        self.assertNotEqual(self.runner1.distance, self.runner2.distance, )


if __name__ == "__main__":
    unittest.main()
