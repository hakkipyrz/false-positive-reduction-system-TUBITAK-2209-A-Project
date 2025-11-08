import csv

def display_logs():
  logs_list=[]
  with open('data/Linux_2k.log_structured.csv', mode ='r')as file:
      data_csv = csv.DictReader(file)
      for logs in data_csv:
          logs_list.append(logs)
  return logs_list



#deneme