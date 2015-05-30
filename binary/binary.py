class Binary:
    def __init__(self, b):
        total = 0
        if isinstance(b, str):
            if b.find('x') > 0:
                val = b[1:]
                print 'hex'
            elif b.find('b') > 0:
                val = b[1:]
                print 'bit'
            else:
        elif isinstance(b, list):
            '''reverse the array
            '''calculate total popping each list
            for v in list(reverse(b)):
                total += v
            self.b = total
        else:
            self.b = b
