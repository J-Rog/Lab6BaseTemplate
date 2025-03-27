#!/usr/bin/env python3

def print_log(log):
    for i in log:
        print(i)

def print_menu():
    print("1) View Raw Data")
    print("2) List Data")
    print("3) View Select Columns")
    print("4) View Truncated Data")
    print("5) Exit")

def print_columns(log):

    choice = ''
    columns = []
    while(choice != 'n'):
        columns.append(int(input("Which column of data would you like?: ")))
        choice = input("Would you like to select more columns (y/n): ")

        while(choice != 'y' and choice != 'n'):
            print("Invalid option")
            choice = input("Would you like to select more columns (y/n): ")

    columns.sort()

    for i in log:
        for j in columns:
            #print(f"{i=} {j=}")
            print(i[j], end=' ')
        print("\n",end='')

def trunc(word):

    if len(word) < 10:
        return word
    return "Trunc"


if __name__ == "__main__":

    #Note how we can use .read() to get all the data from the file

    file_name = input("Please enter a file name: ")   
    log_stream = open(file_name, 'r')
    log_data_raw = log_stream.read()
    log_stream.close()


    #Here we read in the file line by line using a for loop

    log_stream = open(file_name, 'r')
    log_data = []
    for i in log_stream:
        log_data.append(i.split())
    #Due to how the log file was collected and split the last item may be emptry
    if log_data[-1] == []:
        log_data.pop(-1)
    log_stream.close()
    
    
    program_exit = False
    
    while(not program_exit):
    
        print_menu()
        choice = input("Please select an option: ")
    
    
        if choice == '1':
            print(log_data_raw)
        elif choice == '2':
            print_log(log_data)
        elif choice == '3':
            print_columns(log_data)
        elif choice == '4':
            trunc_list = []
            #We loop over every item in log data and run the map function on it
            for i in log_data:
                 #This calls trunc on every element of i
                 trunc_list.append(list(map(trunc, i)))
            print_log(trunc_list)
        elif choice == '5':
            program_exit = True
        else:
            print("Invalid choice")
    







