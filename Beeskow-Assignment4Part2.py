# Bryce Beeskow
# Assignment 4
# 11/24/2024
# CSC115
# I certify, that this computer program submitted by me is all of my own work. Signed: Bryce Beeskow


#function to read a file 
def read_grades():   
    filename = input("Enter the path to the text file: ")
    grades = []
    
    #try and except to finding a text file
    try:
        with open(filename, 'r') as file:
            for line in file:
                grades.extend(map(float, line.split()))
                print('Data read successfully')        
    except:
        print('No file found')
    return grades

#function to comput statistics by sorting the grades and finding max,min,mean, and median
def statistic_values(grades):
    
    #sorts file and gets the length
    grades.sort()
    n = len(grades)
    
    # finding min, max, mean
    minimum = grades[0]
    maximum = grades[-1]
    mean = sum(grades) / n
    
    #finding median
    if n % 2 == 0:
        median = (grades[n // 2 - 1] + grades[n // 2]) / 2
    else:
        median = grades[n // 2]
        
        #returns those values
    return minimum, maximum, mean, median

#function to save statistics to another text file
def save_statistics(new_file, minimum,maximum, mean, median):
    with open(new_file, 'a') as f:
            f.write(f'Min:    = {minimum}\n')
            f.write(f'Max:    = {maximum}\n')
            f.write(f'Mean:   = {mean}\n')
            f.write(f'Median  = {median}\n')
   


#while loop for user to pick what they want to do with the file
go = 'go'
while go == go:
    print('Choose an option:')
    print('1.  Load data')
    print('2.  Display computed statistics')
    print('3.  Save computed statistics')
    print('4.  Exit')
    choice = int(input('Choice: '))
    print('\n')   
    #if choice is 1 go through the read_grades() function
    if choice ==1:      
        print(read_grades(),'\n')
        
    #else if choice is 2 go through the statistic_values() function    
    elif choice == 2:
        grades = read_grades()
        minimum, maximum, mean, median = statistic_values(grades)
        print('Below are the comput values:')
        print("Sorted list:", grades)
        print("Min:", minimum)
        print("Max:", maximum)
        print("Mean:", mean)
        print("Median:", median, '\n')
    elif choice == 3:
        new_file = input('Enter new file to save to: ')
        minimum, maximum, mean, median = statistic_values(grades)
        save_statistics(new_file, minimum, maximum, mean, median)
    elif choice == 4:
        print('Goodbye')
        break        
    else:
        continue









