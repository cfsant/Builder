import sys, os, threading, subprocess

def main():
    os.system('cls')

    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f'Initialize build on base path {path}...\n')

    subprocess.Popen(['py', 'run-services.py'], creationflags=subprocess.CREATE_NEW_CONSOLE, env=os.environ)
    subprocess.Popen(['py', 'run-client.py'], creationflags=subprocess.CREATE_NEW_CONSOLE, env=os.environ)

main()