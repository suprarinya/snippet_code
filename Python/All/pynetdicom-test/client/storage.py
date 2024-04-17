from pynetdicom import (
     AE, debug_logger, evt, AllStoragePresentationContexts,
     ALL_TRANSFER_SYNTAXES
 )
import json

def get_ipconfig():
    with open('config.txt') as json_file:
        data = json.load(json_file)
        return data

config = get_ipconfig()

debug_logger()

def handle_store(event):
    """Handle EVT_C_STORE events."""
    ds = event.dataset
    ds.file_meta = event.file_meta
    ds.save_as(f'files/{str(ds.SOPInstanceUID)}', write_like_original=False)

    return 0x0000

handlers = [(evt.EVT_C_STORE, handle_store)]

ae = AE()
storage_sop_classes = [
    cx.abstract_syntax for cx in AllStoragePresentationContexts
]
for uid in storage_sop_classes:
    ae.add_supported_context(uid, ALL_TRANSFER_SYNTAXES)

ae.start_server((config['server'], int(config['port'])), block=True, evt_handlers=handlers)