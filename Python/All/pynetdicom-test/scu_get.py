from pydicom.dataset import Dataset

from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind

debug_logger()

def getVALUE(data):
    if data is not None:
        strdata = str(data)
    else:
        strdata = '-'
    return strdata

def get_worklist(value_array,patientname, appointment=None, config=[]):
    ae = AE()
    ae.add_requested_context(PatientRootQueryRetrieveInformationModelFind)

    # Create our Identifier (query) dataset
    ds = Dataset()
    ds.PatientName = patientname
    ds.PatientBirthDate = '*'
    ds.Modality = ''
    ds.SOPInstanceUID = '*'
    ds.AccessionNumber = '*'
    ds.QueryRetrieveLevel = 'PATIENT'
    # ds.PerformedProcedureStepDescription = ''
    # ds.ScheduledProcedureStepStartDate = ''
    # ds.ScheduledProcedureStepSequence = [Dataset()]
    # item = ds.ScheduledProcedureStepSequence[0]
    # item.PerformedProcedureStepDescription = ''
    # item.ScheduledProcedureStepStartDate = ''

    if appointment is not None:
        ds.ScheduledProcedureStepStartDate = appointment

    # Associate with the peer AE at IP 127.0.0.1 and port 11112
    assoc = ae.associate(config['server'], int(config['port']))
    if assoc.is_established:
        # Send the C-FIND request
        responses = assoc.send_c_find(ds, PatientRootQueryRetrieveInformationModelFind)
        for (status, identifier) in responses:
            print('----------identifier---------')
            print(identifier)
            value = {}
            if identifier is not None:
                value['patientname']        = getVALUE(identifier.PatientName)
                value['accessionnumber']    = getVALUE(identifier.AccessionNumber)
                value['patientbirthdate']   = getVALUE(identifier.PatientBirthDate)
                value['modality']           = getVALUE(identifier.Modality)
                value['sopinstanceuid']     = getVALUE(identifier.SOPInstanceUID)
                # value['description']        = getVALUE(identifier.ScheduledProcedureStepSequence[0].PerformedProcedureStepDescription)
                # value['date']               = getVALUE(identifier.ScheduledProcedureStepSequence[0].ScheduledProcedureStepStartDate)
                value_array.append(value)

        # Release the association
        assoc.release()
    else:
        return None

def get_worklist_array(search_txt='*', config=[]):
    value_array = []
    get_worklist(value_array=value_array, patientname=search_txt, config=config)
    return value_array



# print('----------break---------')
# print(get_worklist_array(search_txt='ru'))