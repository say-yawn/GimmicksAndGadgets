import csv

def generate_csv(csv_columns, rolling_metrics_relations, filename):
    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in rolling_metrics_relations:
                writer.writerow(data)
    except:
        return

def read_csv(filename):
    try:
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            datalist = []
            datalist = list(reader)
            return datalist
    except:
        return

def generate_dict_csv(csv_columns, data, filename):
    try:
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in rolling_metrics_relations:
                writer.writerow(data)
    except:
        return

def read_dict_csv(filename):
    try:
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            datalist = []
            datalist = list(reader)
            return datalist
    except:
        return
