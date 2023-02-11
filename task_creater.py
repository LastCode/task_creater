import sys
import uuid

import pandas as pd
import json

# pip install openpyxl

def get_excel_sheetname(file_path=None):
    xl = pd.read_excel(file_path, sheet_name=None)
    sheet_names = xl.keys()
    return list(sheet_names)


### ★★★
def convert_exchel_to_json(file_path=None, json_path=None):
    tasks = []
    data = {}

    # 1. generate json data records
    xl = pd.read_excel(file_path, sheet_name=None)
    for sheet_name in xl.keys():
        df = xl[sheet_name]
        data[sheet_name] = df.to_dict(orient='records')

    # 2. validate each sheet has the same amount of records
    all_record_size = [len(record) for _, record in data.items() ]
    if not all(n == all_record_size[0] for n in all_record_size):
        print(f'Error: data records are not equal!')
        sys.exit()
    record_size = all_record_size[0]

    # 3. convert json to tasks with uuid
    for i in range(record_size):
        task={}
        task_id = str(uuid.uuid4())
        for source, records in data.items():
            task[source]= records[i]
        tasks.append({task_id:task})

    print(tasks)
    # Write the JSON data to a file
    with open(json_path, 'w') as outfile:
        json.dump(tasks, outfile)


if __name__ == '__main__':
    json_path = '/Users/francis/dev/microservices_king/idea/output/data.json'
    file_path = '/Users/francis/dev/microservices_king/idea/data/family.xlsx'

    convert_exchel_to_json(file_path=file_path, json_path=json_path)

