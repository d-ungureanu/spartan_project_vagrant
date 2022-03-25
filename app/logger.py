from datetime import datetime

# Current date and time
now = datetime.now()
# formatting date and time to be used in logger file name
datetime_string = now.strftime("%d%m%y_%H%M%S")
# logger file name
log_file_name = f"log_{datetime_string}.log"


# Function to create the log file
def create_log_file():
    global now
    global datetime_string
    global log_file_name
    with open(log_file_name, "w") as log_file:
        log_file.write(f"{now} - {log_file_name} file created.\n")


# Function to add lines/data to log file
def update_log_file(log_line):
    global log_file_name
    global now
    now = datetime.now()
    with open(log_file_name, "a") as log_file:
        log_file.write(f"{now} - {log_line}\n")