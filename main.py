from notion_functions import insert_values, generate_csv_and_clear_database
import datetime

def inserting():
    print('Please inform the data for the insert:\n')

    expense = input('Expense: ')
    amount = float(input('Amount: '))
    category = input('Category: ')
    comment = input('Comment: ')
    date = input('Date(pls use this format: yyyy-mm-dd or let it blank for get today): ')
    status = input('Status(payed | to pay): ')

    if date == "":
        date = datetime.datetime.now().strftime('%Y-%m-%d')

    page = {
        "Expenses": expense,
        "Amount": amount,
        "Category": category,
        "Comment": comment,
        "Date": date,
        "Status": status
    }

    insert_values(page)

    op = ''
    while op != 'n' or op != 'no':
        op = input('\n Do you want to add more itens(y, yes | n, no): ')

        if op == 'no' or op == 'n':
            print('Ok! Thanks for use the system! See you soon\n')
            break
        elif op == 'yes' or op == 'y':
            inserting()
            break
        else:
            print('Wrong option, please choose y|yes or n|no\n')
            continue

    return None

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