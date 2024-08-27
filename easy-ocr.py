# import warnings
# warnings.simplefilter(action='ignore', category=FutureWarning)
#

import easyocr
reader = easyocr.Reader(['en'])

results = reader.readtext('/home/developer/dmart.jpg')

for result in results:
    text = result[1]
    print(text)