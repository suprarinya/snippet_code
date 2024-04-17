from flask import Flask, render_template, request
from scp import start_worklist_server, stop_worklist_server, get_ipconfig
from scu_get import get_worklist_array
from send import send_file, send_file_client

app = Flask(__name__)

status = None
config = get_ipconfig()
server = config['server']
client = config['client']
port   = config['port']

@app.route("/", methods=['POST', 'GET'])
def home():
    global instance
    global status
    print(status)
    data = None
    if status is None:
        status = 'No connection'

    if request.method == "POST" :
        if 'start' in request.form:
            instance = start_worklist_server(server, int(port))
            if instance is not None:
                status = 'start'
            else:
                status = 'error'
        elif 'stop' in request.form:
            if instance is not None:
                stop_worklist_server(instance)
            status = 'stop'
        elif 'get_all' in request.form:
            data = get_worklist_array(config=config)
        elif 'get_today' in request.form:
            print('disabled')
        elif 'send_to_server' in request.form:
            file_name = request.form.get('file_name')
            send_file(file_name, config)
        elif 'search' in request.form:
            search_txt = request.form.get('search_txt')
            data = get_worklist_array(search_txt=search_txt, config=config)
        elif 'send' in request.form:
            file_to_send = request.form.get('send')
            send_file_client(file_path=file_to_send, config=config)

        print(data)
    return render_template('index.html', status=status, data=data, config=config)
if __name__ == '__main__':
    app.run(debug=True)