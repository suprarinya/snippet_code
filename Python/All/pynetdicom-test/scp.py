import os
import json
from pydicom import dcmread
from pydicom.dataset import Dataset
from pynetdicom import (
     AE, debug_logger, evt, AllStoragePresentationContexts,
     ALL_TRANSFER_SYNTAXES
 )
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind

def getVALUE(data):
    if data is not None:
        strdata = str(data)
    else:
        strdata = '-'
    return strdata

def handle_assoc_reject(event):
    print('{0}: {1}'.format(
        event.assoc.acceptor.primitive.result_str, 
        event.assoc.acceptor.primitive.reason_str
    ))

def handle_store(event):
    """Handle EVT_C_STORE events."""
    ds = event.dataset
    ds.file_meta = event.file_meta
    ds.save_as(f'files/{str(ds.SOPInstanceUID)}', write_like_original=False)

    return 0x0000

def get_ipconfig():
    with open('config.txt') as json_file:
        data = json.load(json_file)
        return data

# Implement the handler for evt.EVT_C_FIND
def handle_find(event):
    """Handle a C-FIND request event."""
    ds = event.identifier

    # Import stored SOP Instances
    instances = []
    fdir = 'files'
    for fpath in os.listdir(fdir):
        instances.append(dcmread(os.path.join(fdir, fpath)))

    if 'QueryRetrieveLevel' not in ds:
        # Failure
        yield 0xC000, None
        return

    matching = []
    if ds.QueryRetrieveLevel == 'PATIENT':
        if 'PatientName' in ds:
            for inst in instances:
                if ds.PatientName in ['*']:
                    matching.append(inst)
                elif ds.PatientName not in ['*']:
                    if str(ds.PatientName).lower() == str(inst.PatientName).lower() or str(ds.PatientName).lower() in str(inst.PatientName).lower() or str(ds.PatientName).lower() in str(inst.PatientName).lower():
                        matching.append(inst)

            # Skip the other possible values...

        # Skip the other possible attributes...

    # Skip the other QR levels...
    value_array = []
    for instance in matching:
        # Check if C-CANCEL has been received
        if event.is_cancelled:
            yield (0xFE00, None)
            return

        yield (0xFF00, instance)

handlers = [(evt.EVT_C_FIND, handle_find), 
            (evt.EVT_REJECTED, handle_assoc_reject),
            (evt.EVT_C_STORE, handle_store)]

# Initialise the Application Entity and specify the listen port
ae = AE()

# Add the supported presentation context
ae.add_supported_context(PatientRootQueryRetrieveInformationModelFind)
storage_sop_classes = [
    cx.abstract_syntax for cx in AllStoragePresentationContexts
]
for uid in storage_sop_classes:
    ae.add_supported_context(uid, ALL_TRANSFER_SYNTAXES)

# Start listening for incoming association requests
# server = ae.start_server(("192.168.1.63", 11112), evt_handlers=handlers)

def start_worklist_server(server_ip, port):
    try:
        start = ae.start_server((server_ip, port), evt_handlers=handlers, block=False)
    except:
        start = None
    return start

def stop_worklist_server(instance):
    instance.shutdown()

# start_worklist_server()
