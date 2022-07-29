**Assignments from Week 6 of CS50's Introduction to Programming with Python at Harvard**

Week 6 was spent learning about **File IO**. Below are descriptions of each of the programs in this folder:  
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------
  
**scourgify.py**: Expects the user to provide two command-line arguments:  
  
1. The name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house. Like the following:
  
   name,house  
   "Abbott, Hannah",Hufflepuff  
   "Bell, Katie",Gryffindor  
   "Bones, Susan",Hufflepuff  
   "Boot, Terry",Ravenclaw  
   "Brown, Lavender",Gryffindor  
   "Bulstrode, Millicent",Slytherin  
   "Chang, Cho",Ravenclaw  
  
2. The name of a new CSV to write as output, whose columns should be, in order, first, last, and house. Like the following:

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
  
**
