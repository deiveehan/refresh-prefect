from prefect import task, Flow
import csv


@task
def extract(path):
    print("extracting data")
    with open(path, 'r') as f:
        text = f.readline().strip()
    data = [int(i) for i in text.split(',')]
    return data

@task
def transform(data):
    print("transform")
    tdata = [i+1 for i in data]
    return tdata

@task
def load(data, path):
    print("load")
    with open(path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    return True

with Flow("my_etl") as flow:
    data = extract("02-data.csv")
    tdata = transform(data)
    load(tdata, "02-tdata.csv")
    flow.run()