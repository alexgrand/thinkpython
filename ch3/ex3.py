
def beam(columns):
    beam = '+' + ' - ' * 4
    return beam * columns + '+\n'

def post(columns):
    post = '|' + '   ' * 4
    return post * columns + '|\n'

def draw(columns_num, rows_num):
    row = beam(columns_num)
    row += (post(columns_num) * 4 + beam(columns_num)) * rows_num

    print(row)

draw(2, 2)