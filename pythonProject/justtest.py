import subprocess

command = "echo 11"
subprocess.run("runas /user:Administrator " + command, shell=True)