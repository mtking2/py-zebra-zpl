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

label.dump_contents()
