import unittest

from unittest.loader import makeSuite

from test_cases.login_to_the_system import TestLoginPage
from test_cases.test_player import TestPlayerPage


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestPlayerPage))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
