**Assignments from Week 6 of CS50's Introduction to Programming with Python at Harvard**

Week 6 was spent learning about **File IO**. Below are descriptions of each of the programs in this folder:  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**scourgify.py**: Expects the user to provide two command-line arguments other than the filename ---   
  
**1.** The name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house. Like the following:
  
   name,house  
   "Abbott, Hannah",Hufflepuff  
   "Bell, Katie",Gryffindor  
   "Bones, Susan",Hufflepuff  
   "Boot, Terry",Ravenclaw  
   "Brown, Lavender",Gryffindor  
   "Bulstrode, Millicent",Slytherin  
   "Chang, Cho",Ravenclaw  
  
**2.** The name of a new CSV to write as output, whose columns should be, in order, first, last, and house. Like the following:

   first,last,house  
   Hannah,Abbott,Hufflepuff  
   Katie,Bell,Gryffindor  
   Susan,Bones,Hufflepuff  
   Terry,Boot,Ravenclaw  
   Lavender,Brown,Gryffindor  
   Millicent,Bulstrode,Slytherin  
   Cho,Chang,Ravenclaw  
  
Converts the input CSV to the format of the output CSV, splitting each name into a first name and last name. Then, writes the resulting data to the output CSV.
  
NOTE: If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**shirt.py**: Expects exactly two command-line arguments other than the filename ---  
  
**1.** In sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input  
**2.** In sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output  
  
Then, overlays shirt.png (an image of a shirt with a transparent background) on the input after resizing and cropping the input to be the same size. Lastly, saves the result to the output.  
  
NOTE: The program exits via sys.exit:  
**1.** If the user does not specify exactly two command-line arguments.  
**2.** If the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively.  
**3.** If the input’s name does not have the same extension as the output’s name.  
**4.** If the specified input does not exist.  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**pizza.py**: Expects exactly one command-line argument other than the filename --- the name (or path) of a CSV file in Pinocchio's format. Here is an example of a pizza menu in said format:
  
   Sicilian Pizza,Small,Large  
   Cheese,$25.50,$39.95  
   1 item,$27.50,$41.95  
   2 items,$29.50,$43.95  
   3 items,$31.50,$45.95  
   Special,$33.50,$47.95  
  
Then, outputs the data from the input CSV as a table formatted as ASCII art using the 'tabulate' package. Below is the resulting output of the above pizza menu:

   +------------------+---------+---------+  
   | Sicilian Pizza   | Small   | Large   |  
   +==================+=========+=========+  
   | Cheese           | $25.50  | $39.95  |  
   +------------------+---------+---------+  
   | 1 item           | $27.50  | $41.95  |  
   +------------------+---------+---------+  
   | 2 items          | $29.50  | $43.95  |  
   +------------------+---------+---------+  
   | 3 items          | $31.50  | $45.95  |  
   +------------------+---------+---------+  
   | Special          | $33.50  | $47.95  |  
   +------------------+---------+---------+  

NOTE: If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program instead exits via sys.exit. j          k
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
