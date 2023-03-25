import pyqrcode
import png
from pyqrcode import QRCode

link = 'rudra'
url = pyqrcode.create(link)
url.png('test.png',scale=6)