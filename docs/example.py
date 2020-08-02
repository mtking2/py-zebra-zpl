from zebra_zpl import Label, Text, Barcode

label = Label(width=812, length=1218)

t1 = Text('Hello, ZPL!', font_type=0, font_size=28, width=label.width, y=25, justification='C')
label.add(t1)

bc1 = Barcode('11235813', human_readable='Y', x=100, y=100, width=2, height=100)
label.add(bc1)

label.dump_contents()
