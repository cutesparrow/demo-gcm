import os, sys

# run command that input in command line
# new 111
# new
# new 333
# mew 555
# new2222 
# new 444
# new 666
# new 888
# new 999
# new 10000
# new 100231
# sec fix

def check_cmd(cmd):
    allowed_cmds = ['ls', 'dir', 'echo Hello, World!']
    return cmd in allowed_cmds
if len(sys.argv) > 1 and check_cmd(sys.argv[1]):
    os.system(sys.argv[1])
else: