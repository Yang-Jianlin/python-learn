import os


print('Process (%s) start...', os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process {0} and my parent is {1}'.format(os.getpid(), os.getppid()))
else:
    print('I {0} just created a child process {1}'.format(os.getpid(), pid))
