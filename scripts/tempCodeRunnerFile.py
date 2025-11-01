import csv
with open('data/Linux_2k.log_structured.csv', mode ='r')as file:
    data_csv = csv.reader(file)

    for line in data_csv:
        logs= str(line)
        logs_split= logs.split()
        event_id= logs_split[0]
        print(event_id)