import sys, os

def main():
    os.system('cls')

    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    print(f'Initialize SERVER on base path {path}...\n')

    os.chdir(f'{path}/Services')
    os.system('dotnet build')

    os.chdir(f'{path}/Services/Services')
    os.system(f'dotnet run --project Services.csproj')

main()