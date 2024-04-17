# import os
import json


# from pydicom import dcmread
# from pydicom.dataset import Dataset
# from pynetdicom import (
#      AE, debug_logger, evt, AllStoragePresentationContexts,
#      ALL_TRANSFER_SYNTAXES
#  )
# from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind

# instances = []
# fdir = 'files'
# for fpath in os.listdir(fdir):
#     instances.append(dcmread(os.path.join(fdir, fpath)))
# # print(instances)

# matching = []
# for inst in instances:
#     matching.append(inst)
# # print(matching)


# def get_work(instances):
#     return instances

# data = get_work(instances)
# print(data)
# test = 'Rubo DEMO'.lower()
# if 'Ru'.lower() in test:
#     print('is in') 

# # importing the module
 
# Opening JSON file
def test():
    with open('config.txt') as json_file:
        data = json.load(json_file)
    
        # Print the type of data variable
        print("Type:", type(data))
    
        # Print the data of dictionary
        print("\nPeople1:", data['server'])
        print("\nPeople2:", data['client'])
        return data

data = test()
print(data['server'])