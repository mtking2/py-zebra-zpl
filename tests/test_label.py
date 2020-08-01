import pytest, re, io

from zebra_zpl import Label, Text, InvalidElementError
from zebra_zpl.printable import Printable

def test_init():
    label = Label(width=100, length=200)
    assert label.width == 100
    assert label.length == 200
    assert label.print_speed == 2
    assert label.copies == 1

def test_add():
    label = Label(width=100, length=200)
    t = Text()
    label.add(t)
    assert len(label.elements) > 0
    assert isinstance(label.elements[0], Printable)


def test_invalid_add():
    label = Label(width=100, length=200)
    with pytest.raises(InvalidElementError):
        label.add('bad')

def test_dump():
    label = Label(width=100, length=200)
    t = Text('abc123')
    label.add(t)
    str = io.StringIO()
    label.dump_contents(str)
    zpl = str.getvalue()
    str.close()

    assert re.search(r'\^XA.*\^FDabc123\^FS.*\^XZ', zpl) != None
