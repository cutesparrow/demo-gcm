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
# less allowed command scope

def check_cmd2(cmd):
    # blacklist
    banned_cmds = ['rm', 'del', 'shutdown', 'reboot', 'mkfs', ':(){ :|:& };:', 'format', 'kill', 'taskkill']
    for banned in banned_cmds:
        if banned in cmd:
            return False

if len(sys.argv) > 1 and check_cmd2(sys.argv[1]):
    os.system(sys.argv[1])
else: