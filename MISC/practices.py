import subprocess

for i in range(5):
    subprocess.check_call(["python3", "commands.py"])
    
# We have a list in the subprocess to