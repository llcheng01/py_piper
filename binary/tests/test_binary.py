from binary import Binary

def test_binary_init_int():
    binary = Binary(6)
    assert int(binary) == 6

def test_binary_init_bitstr():
    binary = Binary('110')
    assert int(binary) == 6

def test_binary_init_binstr():
    binary = Binary('0b110')
    assert int(binary) == 6

def test_binary_init_hexstr():
    binary = Binary('0x6')
    assert int(binary) == 6

def test_binary_init_hex():
    binary = Binary('0x6')
    assert int(binary) == 6

def test_binary_init_intseq():
    binary = Binary([1,1,0])
    assert int(binary) == 6

def test_binary_init_strseq():
    binary = Binary(['1','1','0'])
    assert int(binary) == 6
