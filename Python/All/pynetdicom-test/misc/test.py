from pydicom.dataset import Dataset

from pynetdicom import AE, debug_logger, evt
from pynetdicom.sop_class import ModalityWorklistInformationFind, Verification
from datetime import date
import json

#  get date
today = date.today()
dformat = today.strftime("%Y%m%d")

debug_logger()

def handle_assoc_reject(event):
    print('{0}: {1}'.format(
        event.assoc.acceptor.primitive.result_str, 
        event.assoc.acceptor.primitive.reason_str
    ))

def write_json(path, array):
    res = json.dumps(array)
    f = open(path, "w")
    f.write(res)
    f.close()


handlers = [(evt.EVT_REJECTED, handle_assoc_reject)]

# Initialise the Application Entity
ae = AE("FLUX_WORKLIST")

# Add a requested presentation context
ae.add_requested_context(ModalityWorklistInformationFind)
ae.add_requested_context(Verification)

# Create our Identifier (query) dataset
ds = Dataset()
ds.AccessionNumber = '*'
ds.PatientName = '*'
ds.PatientID = '*'
ds.ScheduledProcedureStepSequence = [Dataset()]
item = ds.ScheduledProcedureStepSequence[0]
item.ScheduledStationAETitle = '*'
item.Modality = '*'
item.ScheduledProcedureStepStartDate = dformat
# ds.SequenceDelimitationItem = '*'
# item.Modality = 'CT'

value_array = []
value = {}


# Associate with peer AE at IP 127.0.0.1 and port 11112
assoc = ae.associate("167.172.135.248", 1070, evt_handlers=handlers, ae_title="FLUX_WORKLIST")

if assoc.is_established:

    # Use the C-ECHO service to send the request
    # returns the response status a pydicom Dataset
    # status = assoc.send_c_echo()

    # Use the C-FIND service to send the identifier
    responses = assoc.send_c_find(ds, ModalityWorklistInformationFind)
    for (status, identifier) in responses:
        value = {}
        if status:
            print('C-FIND query status: 0x{0:04x}'.format(status.Status))
            print('----------- break -------------')
            print(identifier)
            if identifier is not None:
                if identifier.PatientName is not None:
                    value['patientname'] = str(identifier.PatientName)
                else:
                    value['patientname'] = '-'

                if identifier.AccessionNumber is not None:
                    value['accessionnumber'] = str(identifier.AccessionNumber)
                else:
                    value['accessionnumber'] = '-'

                if identifier.PatientID is not None:
                    value['patientID'] = str(identifier.PatientID)
                else:
                    value['patientID'] = '-'

                modality = identifier.ScheduledProcedureStepSequence[0].Modality
                if modality is not None:
                    value['modality'] = str(modality)
                else:
                    value['modality'] = '-'

                aetitle = identifier.ScheduledProcedureStepSequence[0].ScheduledStationAETitle
                if aetitle is not None:
                    value['aetitle'] = str(aetitle)
                else:
                    value['aetitle'] = '-'

                date_data = identifier.ScheduledProcedureStepSequence[0].ScheduledProcedureStepStartDate
                if date_data is not None:
                    value['date'] = str(date_data)
                else:
                    value['date'] = '-'

            value_array.append(value)
            print('----------- break -------------')
        else:
            print('Connection timed out, was aborted or received invalid response')

    print(value_array)
    # Release the association
    assoc.release()

    # write json 
    path = "D:/laragon/htdocs/playground/python/pynetdicom-test/json.txt"
    write_json(path, value_array)
else:
    print('Association rejected, aborted or never connected!!!')