
NAME = "log.txt"
def log_event(event, time, id):
    with open(NAME, "a") as file:
        entry = f"ID: {id} |Time: {time} |Event : {event}\n"
        file.write(entry)
    return
