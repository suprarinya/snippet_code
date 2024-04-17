import win32print
import os, sys

printer_name = win32print.GetDefaultPrinter()

if sys.version_info >= (3,):
    raw_data = bytes('This is a test in if', 'utf-8')
else:
    raw_data = 'This is a test in else'

hPrinter = win32print.OpenPrinter(printer_name)
print(hPrinter)

try:
    hJob = win32print.StartDocPrinter(hPrinter, 1, ('test of raw data', None, 'RAW'))
    try:
        print('start printing')
        win32print.StartPagePrinter(hPrinter)
        win32print.WritePrinter(hPrinter, raw_data)
        win32print.EndPagePrinter(hPrinter)
    finally:
        print('close printer')
        win32print.EndDocPrinter(hPrinter)
finally:
    print('close instantly')
    win32print.ClosePrinter (hPrinter)

# print(raw_data)
# print("Printer: %s" % (printer_name))
# p = win32print.OpenPrinter(printer_name)
# print(p)
# job = win32print.StartDocPrinter(p, 1, ("Test Raw text to test the Printer's Raw text printing!", None, "RAW"))
# win32print.StartPrinter(p)
# win32print.WritePrinter(p, "Print Me Puhleeezzz!")
# win32print.EndPagePrinter(p)