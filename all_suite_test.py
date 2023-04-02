import unittest

from unittest.loader import makeSuite

from test_cases.login_to_the_system import TestLoginPage
from test_cases.test_player import TestPlayerPage


def full_suite():
    test_suite = unittest.TestLoader()
    login_test = test_suite.loadTestsFromTestCase(TestLoginPage)
    player_test = test_suite.loadTestsFromTestCase(TestPlayerPage)
    return unittest.TestSuite([login_test, player_test])


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
