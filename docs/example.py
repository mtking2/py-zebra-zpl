from zebra_zpl import Label, Text, Barcode

label = Label(width=609, length=507.5)

t1 = Text('Hello, ZPL!', font_type=0, font_size=28,
          position=(0, 25), width=label.width, y=25, justification='C')

label.add(t1)

qr_code = Barcode('11235813', type='Q', magnification=5, mode='2',
                  position=(label.width/2.5, 25), width=2, height=100)

label.add(qr_code)

label.dump_contents()
