import os
import subprocess
import random
import time

def run_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout.strip()

def modify_file(file_name, content):
    with open(file_name, "a") as file:
        file.write(content)

def commit_and_push(file_name, commit_message, branch="main"):
    run_command("git add .")
    run_command(f'git commit -m "{commit_message}"')
    run_command(f"git push origin {branch}")

file_name = "dummy.txt"
commit_count = int(input("How many commits do you want to add? "))
branch = input("Enter the branch name (default: main): ") or "main"
commit_messages = [
    "Small update to the file",
    "Automated commit",
    "Updated content in dummy.txt",
    "Testing automated git push",
    "Making incremental changes",
    "Adding new lines to the file",
    "Random content update"
]

if __name__ == "__main__":
    if not os.path.exists(".git"):
        print("Error: This script must be run inside a Git repository.")
        exit(1)
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            file.write("Initial content\n")
    for i in range(commit_count):
        message = random.choice(commit_messages)
        content = f"{message} - {time.ctime()}\n"
        print(f"Modifying file and creating commit {i+1}/{commit_count}: {message}")
        modify_file(file_name, content)
        commit_and_push(file_name, message, branch)
        time.sleep(1)
    print(f"Successfully created and pushed {commit_count} commits to branch '{branch}'!")
