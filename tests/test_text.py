import pytest, re, io

from zebra_zpl import Text
from zebra_zpl.printable import Printable

def test_init():
    with pytest.raises(TypeError):
        Text()
    with pytest.raises(ValueError):
        Text('')
    
    t = Text('abc123')
    assert isinstance(t, Printable)

def test_attributes():
    t = Text('abc123', font_type='D', font_size=12)
    assert t.data is 'abc123'
    assert t.font_type is 'D'
    assert t.font_size is 12
    assert t.max_lines is 1
    assert t.line_spacing is 0
    assert t.hanging_indent is 0

def test_invalid_attributes():
    with pytest.raises(ValueError):
        Text('abc123', font_type='a')
    with pytest.raises(ValueError):
        Text('abc123', font_type=-1)
    with pytest.raises(ValueError):
        Text('abc123', font_type=10)
    with pytest.raises(ValueError):
        Text('abc123', font_size=-1)
    with pytest.raises(ValueError):
        Text('abc123', font_size=32001)

def test_zpl():
    t = Text('abc123', font_type='D', font_size=12)
    assert t.to_zpl() == '^FWN^CFD,12^CI28^FO0,0^FB0,1,0,L,0^FDabc123^FS'
    