"""Run a small, real red-green-refactor demonstration without editing calculator.py."""
import unittest


def run_check(label, implementation):
    class AdditionTests(unittest.TestCase):
        def test_one_plus_one(self):
            self.assertEqual(implementation(1, 1), 2)

        def test_one_plus_two(self):
            self.assertEqual(implementation(1, 2), 3)

    print(f'\n{label}', flush=True)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(AdditionTests)
    return unittest.TextTestRunner(verbosity=1).run(suite).wasSuccessful()


def main():
    def stub(first, second):
        pass

    def constant(first, second):
        return 2

    def general(first, second):
        return first + second

    def refactored(first, second):
        """Give the same addition behaviour a clear, documented contract."""
        return first + second

    outcomes = [
        run_check('RED: empty implementation; both tests should fail', stub),
        run_check('RED: hard-coded result; second test should still fail', constant),
        run_check('GREEN: general addition; both tests should pass', general),
        run_check('REFACTOR: add the contract; behaviour should stay green', refactored),
    ]
    if outcomes != [False, False, True, True]:
        raise SystemExit('The demonstration did not behave as expected')
    print('\nThe expected red, red, green, green sequence was verified.')


if __name__ == '__main__':
    main()
