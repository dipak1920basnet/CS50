from bank import value
def test_hello():
    assert value("hello sir") == 0
    assert value("Hello madam") == 0

def test_h():
    assert value('hy sir') == 20
    assert value('hey sir') == 20
    assert value("how are you sir") == 20
    assert value("How is it hanging bro?") == 20
