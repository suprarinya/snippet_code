from datetime import datetime
import json
import os
import tempfile
import base64
import numpy as np
import random 
import sys
import base64
import codecs

import pydicom
from pydicom.dataset import FileDataset, FileMetaDataset
from pydicom.uid import UID

from PIL import Image


# base64str  = "eyJtb2RhbGl0eSI6IlVTIiwiY2FzZXVuaXEiOjIyMTIxNTA5Mjc1NCwiaG4iOiJURVNUMjAyMjExMTEiLCJmaXJzdG5hbWUiOiJ0ZXN0IiwibGFzdG5hbWUiOiJ0ZXN0IiwiZGF0ZXRpbWUiOiIxNTM2MTAiLCJnZW5kZXIiOiJNIiwiYWdlIjowLCJzdHVkeWRhdGUiOiIyMDIzMDMyNSIsImNhc2VkYXRlIjoiMjAyMy0wMy0yNSIsImNhc2V0aW1lIjoiMDg6MDA6MDAiLCJwcm9jZWR1cmUiOiJFR0QiLCJiaXJ0aGRhdGUiOiIxOTc3LTAxLTAxIiwid2FyZCI6InRlc3QiLCJkb2N0b3JuYW1lIjoi4LitLuC4geC4o+C4geC4iiDguYDguIHguKnguJvguKPguLDguYDguKrguKPguLTguJAiLCJhY2Nlc3Npb25OVU1CRVIiOiIiLCJmb2xkZXJkYXRlIjoiMjAyMi0xMi0xNSJ9" 

try:
    # base64.b64decode(sys.argv[1]).decode('utf-8')
    # endoget = base64.b64decode(base64str)
    endoget = base64.b64decode(sys.argv[1])
    s = endoget.decode("utf-8")




    # aaa    = json.JSONDecoder(endoget);
    dict_obj = json.loads(s)

    img_width   = dict_obj.get('width')
    img_height  = dict_obj.get('height')
    caseuniq    = str(dict_obj.get('caseuniq'))
    modality    = str(dict_obj.get('modality'))
    studydate   = str(dict_obj.get('studydate'))
    hn          = str(dict_obj.get('hn'))
    patientname = str(dict_obj.get('patientname'))
    # pname       = str(dict_obj.get('patientname')).encode()
    dt          = str(dict_obj.get('datetime'))
    gender      = str(dict_obj.get('gender'))
    age         = str(dict_obj.get('age'))
    casedate    = str(dict_obj.get('casedate'))
    casetime    = str(dict_obj.get('casetime'))
    procedure   = str(dict_obj.get('procedure'))
    birthdate   = str(dict_obj.get('birthdate'))
    ward        = str(dict_obj.get('ward'))
    doctorname  = str(dict_obj.get('doctorname'))


    ''' 
    f = codecs.open(caseuniq+".txt", "a", "utf-8")
    f.write(caseuniq)
    f.write('\n')
    f.write(hn)
    f.write('\n')
    f.write(firstname)
    f.write('\n')
    f.write(lastname)
    f.write('\n')
    f.write(dt)
    f.write('\n')
    f.write(gender)
    f.write('\n')
    f.write(age)
    f.write('\n')
    f.write(casedate)
    f.write('\n')
    f.write(casetime)
    f.write('\n')
    f.write(procedure)
    f.write('\n')
    f.write(birthdate)
    f.write('\n')
    f.write(ward)
    f.write('\n')
    f.write(doctorname)
    f.write("aaaaaaaaaaaaa")
    f.close()
    '''

    # folder_path = 'D:/laragon/htdocs/store/TEST20220925/2022-09-25/temp'
    folder_path = 'D:/laragon/htdocs/store/'+dict_obj.get('hn')+'/'+dict_obj.get('casedate')+'/temp'


    # Create some temporary filenames
    suffix                  = '.dcm'
    filename_little_endian  = tempfile.NamedTemporaryFile(suffix=suffix).name
    filename_big_endian     = tempfile.NamedTemporaryFile(suffix=suffix).name

    # Populate required values for file meta information
    meta                            = pydicom.Dataset()
    meta.TransferSyntaxUID          = pydicom.uid.ExplicitVRLittleEndian

    # Secondary Capture Image Storage
    # 1.2.840.10008.5.1.4.1.1.7


    # 1.2.840.10008.5.1.4.1.1.77.1.1 //ES
    # meta.MediaStorageSOPClassUID    = UID('1.2.840.10008.5.1.4.1.1.77.1.1')
    # 1.2.840.10008.5.1.4.1.1.2 //CT
    meta.MediaStorageSOPClassUID    = UID('1.2.840.10008.5.1.4.1.1.7')
    meta.MediaStorageSOPInstanceUID = pydicom.uid.generate_uid()
    # meta.MediaStorageSOPInstanceUID = "1.08.1982.10121984.2.0.07.637504417373475646"
    # # build dataset
    ds = FileDataset(filename_little_endian, {},file_meta=meta, preamble=b"\0" * 128)

    # # unknown options
    ds.is_little_endian         = True
    ds.is_implicit_VR           = False
    ds.SpecificCharacterSet     = 'ISO_IR 166'
    ds.SOPClassUID              = UID('1.2.840.10008.5.1.4.1.1.7')
    # ds.SOPInstanceUID           = "1.08.1982.10121984.2.0.07.637504417373475646"
    ds.SeriesInstanceUID        = pydicom.uid.generate_uid()
    ds.StudyInstanceUID         = pydicom.uid.generate_uid()
    ds.FrameOfReferenceUID      = pydicom.uid.generate_uid()
    # ds.SeriesInstanceUID        = "1.08.1982.10121984.2.0.07.637504417373475646"
    # ds.StudyInstanceUID         = "1.08.1982.10121984.2.0.07.637504417373475646"
    # ds.FrameOfReferenceUID      = "1.08.1982.10121984.2.0.07.637504417373475646"

    ds.ImagesInAcquisition = "1"
    ds.InstanceNumber = 1
    ds.ImagePositionPatient = r"0\0\1"
    ds.ImageOrientationPatient = r"1\0\0\0\-1\0"
    ds.ImageType = r"ORIGINAL\PRIMARY\AXIAL"
    ds.RescaleIntercept = "0"
    ds.RescaleSlope = "1"

    # # Case options
    ds.PatientName  = patientname.encode('ISO_IR 166')
    ds.PatientBirthDate = dict_obj.get('birthdate')
    ds.PatientAge   = dict_obj.get('age')
    ds.PatientID    = hn
    # ds.ReferringPhysicianName = dict_obj.get('doctorname')
    ds.StudyDate    = studydate
    ds.StudyTime    = casetime
    ds.ContentDate  = studydate
    ds.Modality     = modality

    def decode(image):
        np_image = np.array(image.getdata(),dtype=np.uint8)
        return np_image
    
    def get_extension(filename):
        str_split = filename.split('.')
        ext = str_split[-1]
        return ext


    pixel_data_list = [] 
    pixel_data = ''
    try:
        Input_Image_List = os.listdir(folder_path)
    except: 
        pass
        

    for filenames in Input_Image_List:
        if '.dcm' not in filenames.lower() and '.pdf' not in filenames and '%d' not in filenames:
            filename = folder_path + '/' + filenames
            img = Image.open(filename).convert('RGB')
            # new_img = img.resize((img_width, img_height))
            img.save(filename)

    for filenames in Input_Image_List:
        if '.dcm' not in filenames.lower() and '.pdf' not in filenames and '%d' not in filenames:
            filename = folder_path + '/' + filenames
            img = Image.open(filename).convert("RGB")
            pixel_data = decode(img)
            pixel_data_list.append(pixel_data.tobytes())

    # # required for pixel handler
    ds.BitsStored = 8
    ds.BitsAllocated = 8
    ds.HighBit = 7

    ds.PixelRepresentation = 0
    # 
    
    ds.add_new(0x00280006, 'US', 0)
    ds.add_new(0x00100040, 'CS', gender)        #PatientSex
    ds.add_new(0x00081030, 'LO', procedure)     #Description
    ds.add_new(0x00101010, 'AS', age)           #PatientAge
    ds.add_new(0x0081050, 'PN',  doctorname)           #PatientAge
    # ds.add_new(0x00080060, 'CS', modality)      #Modality
    # ds.add_new(0x00080020, 'DA', studydate)     #StudyDate
    ds.add_new(0x00100030, 'DA', birthdate)     #StudyDate
    
    # ds.add_new(0x00100010, 'PN', PatientName)
    ds.PhotometricInterpretation = "RGB"
    ds.SamplesPerPixel = 3  

    # # grayscale without compression
    # ds.PhotometricInterpretation = "MONOCHROME2"
    # ds.SamplesPerPixel = 1  # 1 color = 1 sampleperpixel
    # ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian

    pixel_data = b"".join(pixel_data_list)
    ds.PixelData = pixel_data + b"\x00" if len(pixel_data) % 2 else pixel_data

    ds.NumberOfFrames = len(pixel_data_list)

    # # Image shape
    ds['PixelData'].is_undefined_length = False
    ds.Columns  = img.width
    ds.Rows     = img.height

    # # validate and save
    pydicom.dataset.validate_file_meta(ds.file_meta, enforce_standard=True)
    # name = str(random.randint(1, 999))
    # extension = get_extension(filename)
    # new_filename = filename.replace(f'.{extension}', name + '.dcm')

    nt = datetime.now()
    
    timenow = str(nt.year) + str(nt.month).zfill(2) + str(nt.day).zfill(2) + str(nt.hour).zfill(2) + str(nt.minute).zfill(2) + str(nt.second).zfill(2)



    newname = "D:\DCM_SCU\Dicom_Target\\"+hn+"_"+timenow+".dcm"
    ds.save_as(newname, write_like_original=False)

    print('success')
except:
    print('nonsuccess')

