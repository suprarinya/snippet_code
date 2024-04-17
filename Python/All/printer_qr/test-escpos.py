from escpos.printer import Usb

#  ใช้ pyusb and libusb-1.0 (ซึ่งเวลาลง escpos จะทำการลง pyusb อยู่แล้ว แต่ต้องลง libusb แยก)
#  คำอธิบายการติดตั้งตัว escpos-printer อยู่ใน "escpos fix issues.pdf" นะคะ

#  Usb(idVendor, idProduct)
p = Usb(0x04b8, 0x0e27)

# จัดสิ่งที่ต้องการพิมพ์ให้ตรงกึ่งกลางของกระดาษ
p.set('CENTER')
# ส่วนของข้อความที่ต้องการจะพิมพ์
p.text("Please scan the QR code below\n")
# ส่วนที่ generate QR code (URL, Error-correction level, size) 
# โดยที่ขนาดอยู่ในช่วง 1-16
p.qr("https://www.lipsum.com/", 1, 8)
# ส่วนที่สั่งให้ตัดกระดาษหรือหยุดการพิมพ์
p.cut()