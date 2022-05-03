import os
import subprocess


def run_on_pipe(cmd: str):
    """
    Any valid linux command (like 'iptables -L') is being redirected to /hostpipe,
    which is a bind volume of a /pipe pipe in the host computer.

    At this point you need to create that pipe with mkfifo /pipe (with chown $USER:$USER
    /pipe and chmod 600 /pipe)

    If the host is runing the script 'pipe_line.sh' provided with this app, the
    command will be executed -and attention to this:- with exactly the same permissions
    that pipe_line.sh is running. So as to run iptables in the host computer you need to
    handle the necessary permissons or run as host (sudo ./pipe_line.sh) if this is docker
    is running in a very, very, very controllated environment...
    """
    cmd = f"echo \"{cmd}\""
    cmdl = cmd.split()
    print('*' * 50)
    print(f"Running: {cmd}")
    try:
        with open('/hostpipe', 'w') as hostpipe:
            subprocess.Popen(cmdl, stdin=hostpipe)
    except FileNotFoundError as fnfe:
        print(f"ERROR: {fnfe}")
    print('*' * 50)