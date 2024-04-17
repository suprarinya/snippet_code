from pydicom.dataset import Dataset

from pynetdicom import AE, debug_logger, evt
from pynetdicom.sop_class import ModalityWorklistInformationFind, Verification

debug_logger()

ae = AE()

# Add a requested presentation context
ae.add_requested_context(ModalityWorklistInformationFind)
ae.add_requested_context(Verification)


def handle_assoc_reject(event):
    print('{0}: {1}'.format(
        event.assoc.acceptor.primitive.result_str, 
        event.assoc.acceptor.primitive.reason_str
    ))

handlers = [(evt.EVT_REJECTED, handle_assoc_reject)]

assoc = ae.associate("127.0.0.1", 11112, evt_handlers=handlers)

if assoc.is_established:
    print("Association established with Echo SCP!")
    assoc.release()
else:
    # Association rejected, aborted or never connected
    print("Failed to associate")

# from datetime import date

# today = date.today()
# d2 = today.strftime("%Y%m%d")
# print("d2 =", d2)
# print("Today's date:", today)

# d1 = today.strftime("%d/%m/%Y")
# print("d1 =", d1)


# val = {}
# val['test'] = 'test'
# print(val['test'])
