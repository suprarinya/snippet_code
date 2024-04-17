import mysql.connector
import os
import json

def connect_mysql(host="127.0.0.1", user="root", password="", database="endo5"):
    cnx = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return cnx

def read_hn(path):
    hns = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    return hns

def get_procedurecode(cursor, procedure_names, format_strings):
    cursor.execute("SELECT procedure_code FROM tb_procedure WHERE procedure_name IN (%s)" % format_strings,
               tuple(procedure_names))
    return [item[0] for item in cursor.fetchall()]

def get_mainpart(cursor, procedure_codes):
    mainpart_list = []
    for code in procedure_codes:
        query = f"""SELECT mainpart_id, mainpart_name FROM tb_mainpart 
        WHERE mainpart_procedure_code = '{code}'
        AND mainpart_name != ''
        """
        cursor.execute(query)
        for item in cursor.fetchall(): 
            mainpart_list.append(item)
    return mainpart_list

def get_mainpartsub(cursor):
    mainpartsub_list = []
    query = "SELECT mainpartsub_id, mainpartsub_name FROM tb_mainpartsub"
    cursor.execute(query)
    for item in cursor.fetchall(): 
        mainpartsub_list.append(item)
    # print(dict(mainpartsub_list))
    return dict(mainpartsub_list)

def check_null(val, is_array=False):
    newval = '' if is_array is False else []
    if val is not None or val:
        newval = val
    return newval

def get_folderdate(datetime):
    foldername = datetime.strftime('%Y-%m-%d')
    return foldername

def change_casephoto(jsonarr, mainpart):
    arr = json.loads(jsonarr)
    mainpart_dict = dict(mainpart)
    for row in arr:
        if row['ns'] == 0:
            continue
        elif row['sc'] != '' and row['sc'] is not None:
            sc_num = int(row['sc'])
            row['sc'] = mainpart_dict[sc_num]
    return arr
        


# cnx = connect_mysql()
# cursor = cnx.cursor()

# pcode = ['gi001', 'gi002', 'uro001', 'gi006']
# mainpart = get_mainpart(cursor, pcode)


# cursor.close()