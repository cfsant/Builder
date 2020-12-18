import sys, os, threading, subprocess

def main():
    # Inicialização
    os.system('cls')
    print(f'Initialize build on base path {os.path.dirname(os.path.abspath(sys.argv[0]))}...\n')

    # Escopo
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    nodemodulespath = f'{path}\\node_modules\\.bin\\'
    inpath = f'{path}\\Protos' 
    outpath = f'{path}\\Client\\proto'

    if not os.path.isdir(outpath):
        os.system(f'mkdir {outpath}')

    # Leitura dos arquivos .proto
    filesnames = ''
    for f in os.listdir(inpath):
        if f.endswith('.proto'):
            filesnames += f'{f} '

    # Criar classes baseadas nos arquivos .proto
    filesnames = filesnames[0:len(filesnames) - 1]
    cmd = f'grpc_tools_node_protoc --plugin=protoc-gen-ts={nodemodulespath}protoc-gen-ts.cmd --js_out=import_style=commonjs,binary:{outpath} --ts_out={outpath} -I {inpath} {filesnames}'
    os.chdir(nodemodulespath) 
    os.system(cmd)

    os.chdir(path) 

    # Executa o serviço gRPC
    subprocess.Popen(['py', 'run-services.py'], creationflags=subprocess.CREATE_NEW_CONSOLE, env=os.environ)

    # Executa o cliente
    subprocess.Popen(['py', 'run-client.py'], creationflags=subprocess.CREATE_NEW_CONSOLE, env=os.environ)

main()