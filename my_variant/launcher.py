import subprocess

subprocess.Popen('python server.py', creationalflag=subprocess.CREATE_NEW_CONSOLE)

subprocess.Popen('python client.py', creationalflag=subprocess.CREATE_NEW_CONSOLE)