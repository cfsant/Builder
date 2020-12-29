import sys, os, threading, subprocess

def main():
    # Inicialização do console
    os.system('cls')
    print(f'Initialize build on base path {os.path.dirname(os.path.abspath(sys.argv[0]))}\n')

    # Escopo
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    nodemodulespath = f'{path}\\node_modules\\.bin\\'
    inpath = f'{path}\\Protos' 
    outpath = f'{path}\\Client\\proto'
    stylesscsspath = f'{path}\\Client\\src\\styles\\scss'
    stylescsspath = f'{path}\\Client\\src\\styles\\css'

    # Instalação dos pacotes npm
    print('- Restore npm packages...\n')
    os.system('npm install')
    print('\nRestore npm packages compleate.\n')

    # Validação do diretório de saída
    print('- Output directory validations...')
    if not os.path.isdir(outpath):
        os.system(f'mkdir {outpath}')
        print('Has ben created.\n')
    else:
        print('Was previously created.\n')

    # Leitura dos arquivos .proto
    print('- Read .proto files...')
    filesnames = ''
    filescount = 0
    for f in os.listdir(inpath):
        if f.endswith('.proto'):
            filesnames += f'{f} '
            filescount += 1

    # Validação dos arquivos .proto
    if (filesnames == ''):
        print('No .proto files were found.')
        return
    else:
        filesnames = filesnames[0:len(filesnames) - 1]
        print(f'Read .proto files: {filescount}.')

    # Criar classes baseadas nos arquivos .proto
    print('- Create classes based on .proto files...')
    cmd = f'grpc_tools_node_protoc --plugin=protoc-gen-ts={nodemodulespath}protoc-gen-ts.cmd --js_out=import_style=commonjs,binary:{outpath} --ts_out={outpath} -I {inpath} {filesnames}'
    os.chdir(nodemodulespath) 
    os.system(cmd)

    print('\n- Compile SCSS files...')
    os.system(f"node-sass --watch {}")

    os.chdir(path) 

    # Executa o serviço gRPC
    #print('- Init gRPC Service')
    #subprocess.Popen(['py', 'run-services.py'], creationflags=subprocess.CREATE_NEW_CONSOLE, env=os.environ)

    # Executa o cliente
    print('- Init client')
    subprocess.Popen(['py', 'run-client.py'], creationflags=subprocess.CREATE_NEW_CONSOLE, env=os.environ)

main()