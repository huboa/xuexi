import re
import os
import sys

import re
content='Where are you from? You look so hansome.'
regex=re.compile(r'\w*so4m\w*')
m=regex.search(content)
if m:
    print(m.group(0))
else:
    print("Not found")

