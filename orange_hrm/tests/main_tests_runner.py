import unittest

if __name__ == '__main__':
    # Running all the test here.

    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir='', pattern='test*.py')


    # Run the test suite.
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)