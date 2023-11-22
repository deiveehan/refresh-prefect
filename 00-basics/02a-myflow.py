from prefect import task, Flow
import csv

# Task to extract data from a CSV file
@task
def extract(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        data = [list(map(int, row)) for row in reader]
    return data

# Task to transform data by incrementing each integer by 1
@task
def transform(data):
    return [[value + 1 for value in row] for row in data]

# Task to load data into a new CSV file
@task
def load(data, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Define the flow
with Flow("ETL Flow") as flow:
    extracted_data = extract("02a-myflow.csv")
    transformed_data = transform(extracted_data)
    load(transformed_data, "output.csv")

# Visualize the flow
flow.visualize()

# Run the flow
flow.run()
