#1. Open the filenames.txt file with read-only access with the open() function

file_obj = open('filenames.txt','r')

print(file_obj)

file_obj.close()


#2. Print the name of the file and if it is open or closed using the .name and .closed properties

exer2 = open('filenames.txt','r')
print("What is the file Name?: ", exer2.name)
print("Is the file closed?: ", exer2.closed)

exer2.close()
print("Is the file closed?: ", exer2.closed)

#3. Use a for loop to read all lines of filenames.txt into a list variable

exer3 = open('filenames.txt','r')

for line in exer3:
    print(line)
 

#4. Print out all the lines from the file from your variable
#exer4 = open('filenames.txt','r')

#for 

#5. Close the filenames.txt file and print if the file is open or closed

#6. Create a file using the open() function called secrets.txt

#7. Write your own secrets to the file with the write() function

#8. Close the secrets.txt file using the close() method. DON'T FORGET!

#9. Print out the contents of the text file in your terminal to prove it worked

#10. Open your secrets.txt file in append mode and write some more super secret info

#11. Close the secrets.txt file again using the close() function

#12. Rename the secrets.txt and make it a "hidden" file named .supersecret.txt using the os.rename() function


#13. See if you can see the file in your file explorer

#14. Create a list variable named file_names that contains a list of filenames

#file_names[one.tx]

#15. Use the writelines() function to append the filenames to the filenames.txt file

file_names = ('\none.txt','\ntwo.txt','\nthree.txt') 

exer_15 = open('filenames.txt','a')

exer_15.writelines (file_names)



#16. Delete the initial secrets.txt file now that you have a super secret hidden version

#17. BOSS LEVEL: Use the input() function to accept user input of a filename to create and create that file.
