# When to write test cases vs just prints or other adhoc testing:

## Test Suites
Testing Suites (e.g. Pytest, Jest, etc.) are good when you're working on a long-term project
* Example: Adding a feature, you might have to change some old code from two weeks, two months, two years, 20 years ago...
    * Testing files are good to run and make sure old code still works as intended
* When to use: For Code Platoon personal project, other projects you actually want to maintain and build on long-term

## Prints and other adhocs 
Print statements and other adhoc ways to test are good for things you're working on short-term
* Example: You got this assignment for school and it has to pass the test cases
    * Prints are fine for testing because after the assignment is done, you're most likely never modifying the code again
* Example: Debugging a problem you're actively fixing
    * Prints are a good debugging tool for when issues come up. You can write new test cases later to prevent the bug afterwards.
* When to use: For Code Platoon 1-2 day assignments, other short-term assignments for continuing education

## Caveat!!
Practice writing test suites on your smaller assignments so you're comfortable writing them on your larger projects.