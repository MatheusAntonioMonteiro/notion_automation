from notion_functions import inserting, generate_csv_and_clear_database

print('------------------------------------------------------------\n')
print('Choose what you want to do: ')
print('1 - Insert new expenses')
print('2 - Close month expenses and generate a CSV file')
choice = ''

while choice != '1' or choice != '2':
    choice = input('#: ')

    if choice == '1':
        inserting()
        break
    elif choice == '2':
        generate_csv_and_clear_database()
        break
    else:
        print('This option does not exist, please choose one in the list!')
    
print('------------------------------------------------------------\n')