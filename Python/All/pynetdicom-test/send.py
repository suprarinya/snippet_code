import subprocess

def send_file(file_path, config):
    server = config['server']
    port = config['port']
    command_line = f'python -m pynetdicom storescu {server} {port} {file_path} -v -cx'
    proc = subprocess.Popen(command_line, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = proc.communicate()


def send_file_client(file_path, config):
    client = config['client']
    port = config['port']
    path = 'files/'
    command_line = f'python -m pynetdicom storescu {client} {port} {path}{file_path} -v -cx'
    proc = subprocess.Popen(command_line, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = proc.communicate()