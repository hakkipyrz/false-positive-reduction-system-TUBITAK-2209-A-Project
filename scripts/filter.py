from main import display_logs

critical_event_ids = ["E13", "E14", "E16", "E17", "E18", "E19", "E27", "E29", "E31", "E47", "E61", "E88", "E116"]
medium_event_ids= ["E9", "E75", "E112"]
low_event_ids= ["E8", "E91", "E101", "E102", "E103"]
ignore_event_ids= ["E1", "E7", "E10", "E12", "E20", "E26", "E28", "E30", "E32", "E46", "E48", "E60", 
"E62", "E70", "E72", "E74", "E76", "E87", "E89", "E90", "E92", "E100", "E104", "E111", "E113", "E115", "E117", "E118"]

critical_logs= []
medium_logs= []
low_logs= []
ignore_logs= []


logs = display_logs()  


for log in logs:

    if log["EventId"] in critical_event_ids:
        critical_logs.append(log)

    elif log["EventId"] in medium_event_ids:
        medium_logs.append(log)
    
    elif log["EventId"] in low_event_ids:
        low_logs.append(log)
    
    elif log["EventId"] in ignore_event_ids:
        ignore_logs.append(log)
    


print("CRITICAL ALERTS:\n")
for i in critical_logs:
    print(str(i))
    print("-"*177)


print("MEDIUM ALERTS:\n")
for i in medium_logs:
    print(str(i))
    print("-"*177)


print("LOW ALERTS:\n")
for i in low_logs:
    print(str(i))
    print("-"*177)


print("IGNORE ALERTS:\n")
for i in ignore_logs:
    print(str(i))
    print("-"*177)