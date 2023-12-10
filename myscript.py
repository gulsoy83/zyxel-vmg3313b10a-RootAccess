import sys
import lzw
import logging as log
import re
import base64
from lxml import etree

import zlib
header=b"<compressed alg=lzw len=26373>          <crc=0x6744189e>    "

with open("testsil.bin", 'rb') as fa:
    fa.read(60)
    compressed_data = fa.read()
    
fa.close()



decoder = lzw.PagingDecoder(initial_code_size=258)
olduncstring = b"".join([b"".join(pg) for pg in decoder.decodepages(compressed_data)])


myfile = open("testsil.txt",'wb')
myfile.write(olduncstring)


myfile.close()




