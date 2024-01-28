#1.Write a python program using function to which will do the following 
  #a.The function will create a text file with current timestamp. 
  #b.The file content should have the content of the current time stamp

#Answer:

import os
print("Current Working Directory:", os.getcwd())

import datetime

def create_timestamp():
    try:
        current_time = datetime.datetime.now()
        timestamp_str = current_time.strftime("%Y-%m-%d_%H-%M-%S")

        file_name = f"timestamp_{timestamp_str}.txt"

        with open(file_name, 'w') as file:
         file.write(f"Timestamp: {timestamp_str}")

        print(f"File '{file_name}' Created Successfully with the timestamp.")
    except Exception as e:
        print(f"Error: {e}")

create_timestamp()

#2.Write another python function to read from text file. The function will take the name of   the text file and display the content of the file into console.

#Answer:

print(end="\n")

def read_and_display_file(file_name):
    try:
      
        with open(file_name, 'r') as file:
            file_content = file.read()

            print(f"Content of the file '{file_name}':\n")
            print(file_content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

read_and_display_file('read.txt')

