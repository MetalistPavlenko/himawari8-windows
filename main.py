from io import BytesIO
from PIL import Image, ImageGrab
import requests, re, os, ctypes, time

def start():
    try:
        p = os.environ['TEMP'] + '\\' + 'Earth.png'
        i = re.findall('(\d+)', requests.get('https://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json').json()['date'])
        i = 'https://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/' + i[0] + '/' + i[1] + '/' + i[2] + '/' + i[3] + i[4] + i[5] + '_0_0.png'
        Image.open(BytesIO(requests.get(i).content)).crop((-ImageGrab.grab().size[0]/2+275, -ImageGrab.grab().size[1]/2+275, ImageGrab.grab().size[0]/2+275, ImageGrab.grab().size[1]/2+275)).save(p)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, p, 0)
        os.popen('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP" /f')
        os.popen('REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP" /v LockScreenImagePath /t REG_SZ /d "'+p+'" /f')
    except:
        time.sleep(5)
        start()
start()
