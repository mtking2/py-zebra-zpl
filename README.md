# zebra-zpl

Python library to generate usable and printable ZPL2 code

## Usage:

```python
from zebra_zpl import Label, Text, Barcode

label = Label(width=812, length=1218)

t1 = Text('Hello, ZPL!', font_size=28, width=label.width, y=25, justification='C')
label.add(t1)

bc1 = Barcode('11235813', human_readable='Y', x=100, y=100, width=2, height=100)
label.add(bc1)

label.dump_contents() #=> ^XA^LL1218^LH0,0^LS10^PW812^PR5^FWN^CF0,28^CI28^FO0,25^FB812,1,0,C,0^FDHello, ZPL!^FS^FWN^FO100,100^BY2,3.0,100^BCN,,Y^FD11235813^FS^PQ1^XZ
```
