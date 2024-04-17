# import usb.core

# dev = usb.core.find(idVendor=0x04b8, idProduct=0x0e27)
# if dev is None:
#     raise ValueError('Devive not found')

# # print(dev)
# # dev.set_configuration()
# print("Read: ", dev.read(0x82, 7))
# print("Write: ", dev.write(1, '0xB1')) 

import usb.core
import usb.util

# from infi.devicemanager import DeviceManager
# dm = DeviceManager()
# devices = dm.all_devices
# for i in devices:
#     try:
#         print ('{} : address: {}, bus: {}, location: {}'.format(i.friendly_name, i.address, i.bus_number, i.location))
#     except Exception:
#         pass

from usb.backend import libusb1

# backend = usb.backend.libusb1.get_backend(find_library=lambda x: "C:\\Windows\\System32\\libusb-1.0.dll")
# dev = usb.core.find(backend=backend, find_all=True)


for dev in usb.core.find(idVendor=0x04b8, idProduct=0x0e27):
    print(dev)

    # it should find libusb-1.0.dll at our path variable
back = libusb1.get_backend()
print(type(back))  # return: <class 'usb.backend.libusb1._LibUSB'>
