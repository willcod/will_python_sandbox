import os

res = os.fork()
print(f'res = {res}')

if res == 0:
    print(f'Child process: {os.getpid()} of parent process: {os.getppid()}')
else:
    print(f'Parent process: {os.getpid()}')