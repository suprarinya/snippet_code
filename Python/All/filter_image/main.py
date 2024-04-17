from functions import *
import shutil

labeled_folder = 'labeled'
count = 0

cnx = connect_mysql()
cursor = cnx.cursor()

procedure_names = ['EGD', 'Colonoscopy', 'Cystoscopy', 'Liver Biopsy']
format_strings = ','.join(['%s'] * len(procedure_names))

procedure_codes = get_procedurecode(cursor, procedure_names, format_strings)
hns = read_hn('asset')
mainpart_dict = get_mainpart(cursor, procedure_codes)
mainpartsub_dict = get_mainpartsub(cursor)
# print(mainpartsub_dict)

conditions = "case_status != 90 AND case_status = 2 AND case_photo != '[]' AND case_hn NOT LIKE '%test%'"

if procedure_codes and hns: 
    procedure_format_strings = ','.join(['%s'] * len(procedure_codes))
    hn_format_strings = ','.join(['%s'] * len(hns))
    
    query = f"""
    SELECT * FROM tb_case 
    WHERE case_status != 90 
    AND case_status = 2 
    AND case_photo != '[]' 
    AND case_hn NOT LIKE '%test%' 
    AND case_procedurecode IN ({procedure_format_strings}) 
    AND case_hn IN ({hn_format_strings})
    """
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(query, tuple(procedure_codes + hns))
    data = cursor.fetchall()
    i = 0
    for row in data:
        i = i + 1
        case_dateappointment = check_null(row['case_dateappointment'])
        case_hn = check_null(row['case_hn'])
        case_photo = check_null(row['case_photo'], is_array=True)
        folderdate = get_folderdate(case_dateappointment)

        print(case_hn, case_dateappointment)

        newcase_photo = change_casephoto(case_photo, mainpartsub_dict)

        for img in newcase_photo:
            count += 1
            if img['ns'] == 0 and img['sc'] == '' and img['tx'] == '':
                continue
            img_path = f'asset/{case_hn}/{folderdate}/'+img['na']
            img_mainpart = img['sc']
            img_other    = img['tx'] 

            if not os.path.exists(img_path):
                continue

            if img_mainpart != '':
                this_path = f'{labeled_folder}/{img_mainpart}'
                if not os.path.exists(this_path):
                    os.makedirs(this_path)
                # shutil.copy(img_path, this_path)

            # if img_other != '':
            #     this_path = f'{labeled_folder}/{img_other}'
            #     if not os.path.exists(this_path):
            #         os.makedirs(this_path)
            #     shutil.copy(img_path, this_path)

            print(img_path, this_path)

        print(f"total {count}")

        # print(case_dateappointment, case_hn, case_photo)
        
else:
    print("No procedure codes found for the given names.")

cursor.close()
cnx.close()