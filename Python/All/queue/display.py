import eel, random
import time
import requests
import json
import os
import socketio
import callsound
import pymongo
from win32      import win32gui
from pymongo    import MongoClient
from datetime   import datetime
import pyautogui


f          = open("config/mongo_config.json", "r")
mconfig    = json.loads(f.read())
host       = mconfig[0]["host"]
port       = mconfig[0]["port"]
collection = mconfig[0]["collection"]
sound_path = "D:/allindex/queue/static/asset/sound/th"

def read_json_file(filename):
    f         = open(f"config/{filename}.json", "r", encoding='utf_8')
    config    = json.loads(f.read())
    return config

def set_hospital_name():
    config    = read_json_file('hospital')
    eel.set_hospital_name(config)

def connect_mongo(host, port, collection, table):
    client = MongoClient(host, port, serverSelectionTimeoutMS=5000, connectTimeoutMS=5000)
    db     = client[collection]
    table  = db[table]
    return client, table

def close_connection(client):
    client.close() 

def count_queue(data):
    count = 0
    try:
        for i in data:
            count = count + 1
    except:
        pass
    return count

def create_where(q_type, q_status):
    where = {}
    where['q_type'] = q_type
    where['q_status'] = q_status
    return where

def get_count_each_queue(host, port, collection, table):
    localclient, localtable = connect_mongo(host, port, collection, table)
    table           = localtable
    count_qcapture  = count_queue(table.find(create_where('001', 'hold'))) + count_queue(table.find(create_where('001', 'normal')))
    count_qfibro    = count_queue(table.find(create_where('002', 'hold'))) + count_queue(table.find(create_where('002', 'normal')))
    count_qbro      = count_queue(table.find(create_where('003', 'hold'))) + count_queue(table.find(create_where('003', 'normal')))
    count_qfollow    = count_queue(table.find(create_where('004', 'hold'))) + count_queue(table.find(create_where('004', 'normal')))
    count_qappoint  = count_queue(table.find(create_where('005', 'hold'))) + count_queue(table.find(create_where('005', 'normal')))
    count_qother    = count_queue(table.find(create_where('006', 'hold'))) + count_queue(table.find(create_where('006', 'normal')))

    close_connection(localclient)

    this_dict = {}
    this_dict['qcapture']   = count_qcapture
    this_dict['qappoint']   = count_qappoint
    this_dict['qfibro']     = count_qfibro
    this_dict['qother']     = count_qother
    this_dict['qbro']       = count_qbro
    this_dict['qfollow']    = count_qfollow

    return this_dict 

def get_queue_type(host, port, collection, table, qnum):
    localclient, localtable = connect_mongo(host, port, collection, table)
    queue = localtable.find_one({"q_number":qnum})
    text = ''
    if isinstance(queue['q_type'], type(None)) is not True:
        print(queue['q_type'])
        if queue['q_type']   == '001':
            text = 'ตรวจส่องกล้อง'
        elif queue['q_type'] == '002':
            text = 'ตรวจผังผืดในตับ'
        elif queue['q_type'] == '003':
            text = 'ตรวจสมรรถภาพปอด'
        elif queue['q_type'] == '004':
            text = 'ติดตามอาการ'
        elif queue['q_type'] == '005':
            text = 'รอทำนัดหมาย'
        elif queue['q_type'] == '006':
            text = 'อื่นๆ'
        else:
            text = 'อื่น ๆ'
    close_connection(localclient)
    return text


def get_queue_history(host, port, collection, table, row=6):
    localclient, localtable = connect_mongo(host, port, collection, table)
    table       = localtable
    queues      = table.find().sort( "_id", pymongo.DESCENDING ).limit(row)
    count_queue = get_count_each_queue(host, port, collection, 'tb_queue')
    eel.render_queuecount(count_queue)

    try:
        for queue in queues:
            print(queue)
            eel.render_queuecallcurrent(queue)
    except:
        print('error')

    close_connection(localclient)


# def clear_queue_otherday():
#     myclient    = pymongo.MongoClient("mongodb://192.168.137.200:27017/")
#     mydb        = myclient["endoindex"]
#     mycol       = mydb["tb_queue"]
#     now         = datetime.now()
#     now_str     = now.strftime("%Y-%m-%d")
#     myquery     = { "q_date": {'$ne': f"{now_str}"} } 
#     print(f"{now_str}")
#     mycol.delete_many(myquery)
# clear_queue_otherday()

sio = socketio.Client()
while True:
    try:
        sio.connect('http://endoindex:3000')
        break
    except:
        time.sleep(1)

@sio.on('queue')
def on_message(data):
    print('queue',data)
    if 'calling' in data:
        q_json   = json.loads(data)
        q_number = q_json['calling']
        q_type   = get_queue_type(host, port, collection, 'tb_queue', q_number)
        eel.set_current_queue(q_number, q_type)
        callsound.play_sound(q_number, sound_path)
    elif 'refreshcount' in data:
        qcount = get_count_each_queue(host, port, collection, 'tb_queue')
        eel.render_queuecount(qcount)

dirname = os.path.dirname(__file__)
eel.init("web")
eel.start("display03.html", block=False, size=(1980, 1024),position=(-300,-250), port= 5000,mode='chrome-app')
# eel.start('display03.html', mode='chrome-app', port=8080, cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])
set_hospital_name()
get_queue_history(host, port, collection, 'tb_queuecallcurrent')

f11 = True
while True:
    eel.sleep(3.0)

    if f11:
        eel.sleep(1.0)
        f11 = False
        pyautogui.press("f11")



