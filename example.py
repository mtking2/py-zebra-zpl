import zebra_zpl as zpl

label = zpl.Label(width=812, length=1218)
t1 = zpl.Text('hello', font_size=28, width=label.width, justification='C')
label.add(t1)

bc1 = zpl.Barcode('11235853', human_readable='Y', x=100, y=100, width=2, height=100)
label.add(bc1)

label.dump_contents()
