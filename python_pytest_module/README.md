## Installation
`python --version` to check your Python version
`pip install pytest`

## NOTES
test module and our test function must contain the prefix "test_". 
When pytest runs, it will discover tests from its current directory down. 
By default, any function names with the prefix "test_" in any modules with the prefix "test_" will be identified and executed as test cases.
Note that you may also put non-test functions inside test modules.

`@pytest.mark.skip` To skip a specific test case
`@pytest.mark.<markerName>` to 'tag' a test case. Ensure that your markerName is also in the pytest.ini file

`@pytest.fixtures` 
Fixtures are functions usually for setup and cleanup of a test case
A test can call multiple fixtures
Common fixtures can be stored in a "conftest.py" module under the "tests" directory.


## Running Tests
Enter any of following commands from the project's root directory.
`python -m pytest`
`python -m pytest -v` to show pass fail per test case
`python -m pytest --quiet` to display summary only
`python -m pytest --exitfirst` to exit instantly on first error or failed test.

Filtering To run a specific test: 
`python -m pytest <path>::<test_case_name>`
i.e python -m pytest tests/test_math.py::test_one_plus_one

`python -m pytest -k one` 
This runs tests with key = one

`python -m pytest -m math`
Gets all with marker = math @pytest.mark.math (markers are like test tags. They are also defined in pytest.ini)

TEST RESULTS: 
`.` = passed
`F` = failed - By default, pytest will print test code snippets, failure reasons, and test result tallies for failed test cases.


## Additional Resources

Python:

* [Python.org](https://www.python.org/)
* [pytest.org](https://docs.pytest.org/)
* [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
* [Effective Python Testing with Pytest](https://realpython.com/pytest-python-testing/)

Books:

* [Python Testing with pytest](https://pragprog.com/titles/bopytest/) by Brian Okken
* [pytest Quick Start Guide](https://www.packtpub.com/web-development/pytest-quick-start-guide) by Bruno Oliveira
* [Test-Driven Development with Python](https://www.obeythetestinggoat.com/) by Harry J.W. Percival
