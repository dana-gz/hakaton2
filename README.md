<h1>__Teacher's Generator__


<h3>Script in Python

<h4>Uses csv module and class csv.DictReader to read the  data from csv file

<h4>An example of import .txt and .csv file


The script helps a teacher to prepare messages to be sent to his students at the end of the school year. 

It imports the data from a table in a csv file [_students.csv_] and on ist base creates messages for students.Each student receives an information about the tasks still  required to be submitted, the grade and the possibility to raise it up. 

The message is imported form txt file [_message.txt_]. It makes it easy to edit the message in case it is necessary.


For both files [_students.csv_message.txt_] exceptions are written, so as to prevent problems caused by erros [_FileNotFoundError_] resulted by a missing file csv or txt or a change of a file name. Exception is written also so as to prevent problems caused by absence of message read from the file txt [_NameError_].

Writen as a task in hackathon - elements of script's code come from preparation files for the task.

This project is licensed under the terms of the MIT license.
 
