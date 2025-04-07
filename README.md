# LT 

Overview

This LT repository consist of is a Python-based tool that processes CSV files to identify the top student based on their marks. The script reads the CSV file, identifies the columns containing student numbers and marks, and determines the top student.

# Features

- Reads CSV files
- Identifies columns containing student numbers and marks
- Transversers through the table in the csv file
- outputs the best student, by outputting the highest mark and then the corresponding studentnumber of the student who obtained it 

# Requirements

- Python 3
- command prompt
- ssh key
- https://github.com/nixkj/lt
- nano 
  

# Setup

1. Clone the repository:
    git clone https://github.com/KulaniKhoza/lt.git
    add collaborators in settings of the professors
   add a read me file inside ur github and write your name 

2. Go to the project directory:
 
  -  cd lt (to be in ur repository)
  -  create a dev branch : git branch dev
  -  switch to ur branch : git checkout dev
  -  Edit ur read me to create a first commit and test if ur in the right directory and everything is working:
      touch README.md
      nano README.md
      * edit and add a relevant text *      
     git commit -a -m "Read me test change"
- simply push the changes to the dev branch: git push origin dev
  if everything seems to be working nicely, move on to 3
  
  3. Organize ur filing in the repo for appropriate testing
      - since the repository ur previously cloned has csv file and the getbest.py file nicely in order simple add the test file underneath
          touch test_getbest.py
          nano test_getbest.py
          * add some a code: create a unit test class
          git add test_getbest.py
          
        Add the new test file to the staging area
    git add test_getbest.py

      Commit the changes:
 
  git commit -m "Add unit test for getbest.py"


  Push the changes to the dev branch:

   git push origin dev
    


# Usage

To use the script, run the following command:


python3 getbest.py bestdat0.csv 

To edit your script: 

nano getbest.py   

From there onwards commit and push to dev branch 


## Explanation of the Code

## getbest.py

#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''
    headings = f.readline().strip().split(",")
    i=1
    for head in headings:
        if head == "Student Number": num_col=i
        elif head == "Mark" : mark_col = i+1
    return (num_col, mark_col)

def findTop(f,num_col, mark_col):
    ''' finds the top student in the class '''
    best = best_idx =  0
    for line in f:
        data = line.strip().split(",")
        mark = int(data[mark_col])
        num = int(data[num_col])

        if mark > best:
            best=mark
            best_idx = num
    return best_idx, best

f = open(sys.argv[1])
num_col, mark_col = getCols(f)
best_idx, best = findTop(f,num_col,mark_col)
print("The top student was student %s with %d"%(best_idx,best))


- The `getCols` function takes a list of headings and identifies the columns that contain the "Student Number" and "Mark".
- The `findTop` function takes the data and the indices of the student number and mark columns, and finds the student with the highest mark.
- it loops through the table and the highest mark is declared the best unitl a higher mark is found
- The main block reads the CSV file, processes the headings to find the required columns, and then finds and prints the top student.

## Unit Tests

Unit tests are provided to ensure the correctness of the script. To run the unit tests, use the following command:


python3 -m unittest test_getbest.py


## Explanation of the Unit Test Code

# test_getbest.py

python
import getbest
import unittest
from io import StringIO
class TestingGetBest(unittest.Testcase):

def setUp(self):
self.data = [
            ["ELEN3020", "StudentNumber", "Mark", "Comment"],
            ["ELEN3020", "160001", "72", "OK"],
            ["ELEN3020", "167381", "90", "Check"],
            ["ELEN3020", "143211", "83", "-"]
        ]
def test_getCols(self):
num_col, mark_col = getbest.getCols(self.data[0])
self.assertEqual(num_col, 0)
self.assertEqual(mark_col, 2))

if __name__ == '__main__':
unittest.main()

- The `setUp` method prepares the CSV content as a string.
- The `test_getCols` method tests the `getCols` function with the headers from the CSV content.

Although the unit test didnt work in the end the concept can possibly bring another solution to the problem that a person can look into. especially with a 2d array method.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
