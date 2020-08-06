# zebra-zpl

A Python library to design and generate printable ZPL2 code.

## Usage:

```python
from zebra_zpl import Label, Text, Barcode

label = Label(width=609, length=507.5)

t1 = Text('Hello, ZPL!',
        font_type=0,
        font_size=28,
        width=label.width,
        y=25,
        justification='C')

label.add(t1)

bc1 = Barcode('11235813',
        type='Q',
        magnification=5,
        mode='2',
        position=(100, 50),
        width=2,
        height=100,
        justification='C')

label.add(bc1)

bc2 = Barcode('HelloBarcode',
        type='C',
        human_readable='Y',
        position=(100, 300),
        width=2,
        height=100,
        justification='C')
        
label.add(bc2)

label.dump_contents() #=> ^XA^LL507.5^LH0,0^LS10^PW609^PR2^FWN^CF0,28^CI28^FO0,25^FB609,1,0,C,0^FDHello, ZPL!^FS^FWN,C^FO100,50^BY2,3.0,100^BQN,2,5,M,7^FDMA,11235813^FS^FWN,C^FO100,300^BY2,3.0,100^BCN,100,Y,N,N^FDHelloBarcode^FS^PQ1^XZ
```

## Examples

See [docs/example.py](docs/example.py) for code samples of most elements.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) on how to contribute to this project.

See [CHANGELOG.md](CHANGELOG.md) for a list of changes by version.

## References

###### This library is based on the [zebra-zpl](https://github.com/bbulpett/zebra-zpl) Ruby gem and is meant to serve as a Python3 equivilant to that gem.
* [Zebra Technologies Corporation, _"ZPL II Programming Guide."_ 2019 PDF](https://www.zebra.com/content/dam/zebra/manuals/printers/common/programming/zpl-zbi2-pm-en.pdf)
