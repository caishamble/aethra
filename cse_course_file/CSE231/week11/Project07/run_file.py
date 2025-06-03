#to run this file, uncomment the top part of the code and then run this file
#if you enter 1, this file will run your code with the input from input1.txt
# and output to output1.txt. Then you can match the file with the solution file provided.
#you can use https://www.diffchecker.com/ to compare the files.

import subprocess
n = input("Enter a single-digit test number: ")
myoutput = open("output"+n+".txt","w")
myinput = open("input"+n+".txt",encoding="ascii",errors="surrogateescape")

#IMPORTANT: if you are a MAC user, change 'python' to 'python3' in the line below
p1 = subprocess.check_call(['python',"proj07.py"],stdin=myinput,stdout=myoutput)
myinput.close()
myoutput.close()


