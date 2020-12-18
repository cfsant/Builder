import sys, os

def main():
    os.system('cls')

    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f'Initialize CLIENT on base path {path}...\n')
    
    os.chdir(f'{path}/Client')
    os.system('yarn install')
    print('\n')
    os.system('yarn build')
    print('\n')
    os.system('yarn start')

main()