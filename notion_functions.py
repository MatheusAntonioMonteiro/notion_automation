import requests, json, csv, datetime
from dotenv import dotenv_values

config = dotenv_values(".env")
header = dict(e.split(":") for e in config.get('HEADER').split("\n"))
insert_url = config.get('INSERT_URL')
read_url = config.get('READ_URL')
csv_file_path = config.get('CSVFILEPATH')

def generate_csv_and_clear_database():
    res = requests.post(read_url, headers=header)

    database_values = json.loads(res.text).get('results')

    values = []
    for value in database_values:
        data = {
            "id": value.get('id').replace("-", ""),
            "Expenses": value.get('properties').get('Expenses').get('title')[0].get('plain_text'),
            "Amount": value.get('properties').get('Amount').get('number'),
            "Category": value.get('properties').get('Category').get('multi_select')[0].get('name'),
            "Comment": value.get('properties').get('Comment').get('rich_text')[0].get('plain_text'),
            "Date": value.get('properties').get('Date').get('date').get('start'),
            "Status": value.get('properties').get('Status').get('multi_select')[0].get('name')
        }
        
        values.append(data)

    return save_to_csv(values)


def save_to_csv(values):
    month = datetime.datetime.now().strftime("%B")

    file = open(f"{csv_file_path}expenses_{month}_2022.csv", 'w')
    writer = csv.writer(file)
    writer.writerow(['ID', 'Expenses', 'Amount', 'Category', 'Comment', 'Date', 'Status'])

    for value in values:
        writer.writerow(list(value.values()))

    return clear_database(values)

def clear_database(pages):
    payload = {"archived": True}

    for page in pages:
        page_url = insert_url + page.get('id')
        requests.patch(page_url, json=payload, headers=header)
    
    print('CSV file created and month expenses cloed!')

    return None

def insert_values(page):
    value = {
        "parent": {
            "database_id": config.get('DATABASEID')
        },
        "properties": {
            "Expenses": {
                "title": [{
                    "text": {
                        "content": page.get("Expenses")
                    }
                }]
            },
            "Amount": {
                "number": page.get("Amount")
            },
            "Category": {
                "multi_select": [{
                    "name": page.get("Category")
                }]
            },
            "Comment": {
                "rich_text": [{
                    "text": {
                        "content": page.get("Comment")
                    }
                }]
            },
            "Date": {
                "date": {
                    "start": page.get("Date")
                }
            },
            "Status": {
                "multi_select": [{
                    "name": page.get("Status")
                }]
            }
        }
    }

    requests.post(insert_url, json=value, headers=header)

    print("Item inserido com sucesso!")
    
    return None
 