import usb.core
import usb.backend.libusb1

# # find our device
dev = usb.core.find(idVendor=0x04b8, idProduct=0x0e27)
# print(dev)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)
assert ep is not None

# write the data
ep.write('test')

backend = usb.backend.libusb1.get_backend()
print(backend)

# 
try:
    print(dev.is_kernel_driver_active(interface = 0))
    # if dev.is_kernel_driver_active(interface = 0):
    #     print('if')
        # dev.detach_kernel_driver(interface = 0)
except usb.core.USBError as e:
        print("Kernel detachment failed, please fix this and try again: %s" % str(e))









