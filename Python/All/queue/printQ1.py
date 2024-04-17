# pip install qrcode
import win32print
import win32ui
import win32con
import qrcode
from PIL import Image, ImageWin
from datetime import datetime

def gen_qrcode(url, img_name):
    data = url
    qr = qrcode.QRCode(version = 1,box_size = 15,border = 1)
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save(img_name)

def get_fontsize(hdc,pointsize):
    inch_y = hdc.GetDeviceCaps(win32con.LOGPIXELSY)
    return int(-(pointsize * inch_y) / 72)

def create_font(hDC,name, pointsize, weight):
    font = win32ui.CreateFont({
        "name": name,
        "height": get_fontsize(hDC, pointsize),
        "weight": weight,
    })
    return font

def set_x_text(text):
    char = len(text) - 3
    x = 0.87 - (char * 0.2)
    return x



def printQ(q_number,q_typetext):
    PHYSICALWIDTH   = 110
    PHYSICALHEIGHT  = 111
    scale_factor    = 20
    printer_name    = win32print.GetDefaultPrinter()
    file_name       = "gen.png"
    url_test        = "https://openai.com/"
    gen_qrcode(url_test, file_name)

    hDC = win32ui.CreateDC()

    hDC.CreatePrinterDC(printer_name)
    printer_size = hDC.GetDeviceCaps(
        PHYSICALWIDTH), hDC.GetDeviceCaps(PHYSICALHEIGHT)

    bmp = Image.open(file_name)
    if bmp.size[0] < bmp.size[1]:
        bmp = bmp.rotate(90)

    hDC.StartDoc(file_name)

    hDC.StartPage()
    dib = ImageWin.Dib(bmp)
    # qr code position (left, top, right, bottom) - ขนาดที่ตั้งไว้ ณ ตอนนี้ (200 x 200)
    dib.draw(hDC.GetHandleOutput(), (100, 0, 400, 300))
    # hDC.EndPage()

    now         = datetime.now()
    now_str     = now.strftime("%d/%m/%Y %H:%M")
    queue_txt   = "A01"
    y0 = 3
    y1 = 17.5
    y2 = 17.8
    y3 = 18.1
    y4 = 18.5
    texts   =   [   
        {"x": 0.70, "y": 0.01,  "text": "."},
        {"x": set_x_text(q_number), "y": y0, "text": q_number},
        {"x": 1.00, "y": y1,  "text": q_typetext}, 
        {"x": 0.85, "y": y2,  "text": "แผนก : ส่องกล้อง"}, 
        {"x": 0.70, "y": y3,  "text": f"{now_str}"},
        {"x": 0.70, "y": y4,  "text": "."},
    ]
    hDC.SetMapMode (win32con.MM_TWIPS)

    font        = ''
    for i in range(len(texts)):
        if i == 1:
            font = create_font(hDC,"Prompt-Light", 280, 500)
        else:
            font = create_font(hDC,"Prompt-Light", 90, 400)

        hDC.SelectObject(font)
        hDC.TextOut (   int(scale_factor * 72 * texts[i]['x']),
                        int(scale_factor * 72 * texts[i]['y'] * -1), 
                        texts[i]['text']
                    )
        
    hDC.SelectObject(create_font(hDC,"Prompt-Light", 90, 400))
    hDC.EndDoc()
    hDC.DeleteDC()
