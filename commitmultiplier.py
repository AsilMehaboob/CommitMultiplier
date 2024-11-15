import os
import subprocess
import random
import time


def run_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout.strip()

def create_commit(commit_message, file_name="dummy.txt"):

    with open(file_name, "a") as file:
        file.write(f"{commit_message} - {time.time()}\n")
    

    run_command(f"git add {file_name}")
    

    run_command(f'git commit -m "{commit_message}"')


commit_count = int(input("How many commits do you want to add? "))
commit_messages = [
    "Refactored code",
    "Updated README",
    "Added comments",
    "Improved logic",
    "Minor bug fixes",
    "Code cleanup",
    "Performance improvements",
    "Enhanced documentation"
]

if __name__ == "__main__":
    if not os.path.exists(".git"):
        print("Error: This script must be run inside a Git repository.")
        exit(1)
    
    for i in range(commit_count):
        message = random.choice(commit_messages)
        print(f"Creating commit {i+1}/{commit_count}: {message}")
        create_commit(message)
        time.sleep(1)  
