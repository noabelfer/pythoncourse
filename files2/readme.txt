1.	Implement a function that receives the following arguments:
    a.	file_path (str, a path to a local file)
    b.	start_line (int, line number to start reading from)
    c.	end_line (int, the last line to read)
The function should return a string that contains the lines that have been read. Note, you should check the correctness of the arguments (for example, whether there are enough lines in the file, or whether the file exists). Raise exceptions when needed.



2.	Implement a function that receives a csv file_path (str), and returns the following:
    a.	List of column names
    b.	Number of rows in the file
    c.	Number of columns in the file
Notes:
•	you can assume that the csv file is correct and is not corrupted
•	Consider using DictReader

3.	Implement a function csv2json(). The function receives a file_path of csv file and file_path of a new json file that will be created by a function. The function should read x§the original csv file, convert the data in it into json, and store the contents of the csv file as a json file that contains a list of objects. For example, for this csv file the result should be like this json file
4.	Implement a function json2csv() - the opposite of the previous exercise. This time the function gets the path of the json file (you can assume that the file is actually a list of not nested objects) and creates a corresponding csv file.
5.	Implement a function that receives a directory path (str) as an argument, iterates the given directory, and creates a nested dictionary that corresponds to the structure of the directory and the files in it. For example, for the following directory structure:
 
You the function should create and return the following dictionary:

{
 "fs-7732-3": {
   "dirs": [
     {
       "lesson 8": {
         "dirs": [
           {
             "modules": {
               "dirs": [],
               "files": [
                 "tic_tac.py",
                 "validators.py"
               ]
             }
           }
         ],
         "files": [
           "modules_packages.py",
           "mutability.py",
           "water_hint.py"
         ]
       }
     }
   ],
   "files": []
 }
}

Add an optional argument json_path to the function. The default value for this arg is None, however, 
a new file path can be passed to this argument, and if this is the case - the function should also store the created dictionary 
to a new json file before returning.


