''' Exercise 2: Write a program to prompt for a file name, and then read through the file and look 
for lines of the form: X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the 
floating-point number on the line. Count these lines and then compute the total of the spam confidence 
values from these lines. When you reach the end of the file, print out the average spam confidence. 

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.
'''

fname = input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    exit()
count=0
sum=0
a = len('X-DSPAM-Confidence:')
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        str1=line[a+1:]
        number = float(str1)
        sum=sum+number
print('Average spam number:', sum/count)