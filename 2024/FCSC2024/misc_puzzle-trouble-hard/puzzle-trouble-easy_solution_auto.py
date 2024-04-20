from PIL import Image
import numpy
import math

ct_image = Image.open('puzzle-trouble-hard.jpg')

assert ct_image.format == 'JPEG'
assert ct_image.mode == 'RGB'

ct_length, ct_height = ct_image.size
assert ct_image.size == (1024, 1024)

num_len = 16
block_size_len = ct_length // num_len # Number of blocks on the length
num_hei = 16
block_size_hei = ct_height // num_hei # Numer of blocks on the height

#ct_image.show()

ct_blocks = [[None for _ in range(num_hei)] for _ in range(num_len)]
for i in range(num_len):
    for j in range(num_hei):
        block = Image.new('RGB', (block_size_len, block_size_hei))
        for l in range(block_size_len):
            for h in range(block_size_hei):
                coord = (j * block_size_len + l, i * block_size_hei + h)
                (r, g, b) = ct_image.getpixel(coord)
                block.putpixel((l, h), (r, g, b))
        ct_blocks[i][j] = block

list_blocks = []
for i in range(num_hei):
    for j in range(num_len):
        list_blocks.append(ct_blocks[i][j])

black_block = Image.new('RGB', (block_size_len, block_size_hei))

pt_blocks = [[ct_blocks[2][9], ct_blocks[5][9], ct_blocks[5][10], ct_blocks[4][14], ct_blocks[2][5], ct_blocks[10][3], ct_blocks[11][13], ct_blocks[13][6], ct_blocks[6][3], ct_blocks[1][10], ct_blocks[14][5], ct_blocks[15][6], ct_blocks[2][6], ct_blocks[3][9], ct_blocks[7][5], ct_blocks[5][4]],
            [ct_blocks[12][5], ct_blocks[4][2], ct_blocks[13][1], ct_blocks[3][11], ct_blocks[7][4], ct_blocks[9][2], ct_blocks[6][10], ct_blocks[15][8], ct_blocks[3][14], ct_blocks[6][15], ct_blocks[5][12], ct_blocks[7][8], ct_blocks[10][15], ct_blocks[5][13], ct_blocks[9][11], ct_blocks[4][9]],
            [ct_blocks[11][6], ct_blocks[12][11], ct_blocks[12][4], ct_blocks[11][2], ct_blocks[15][4], ct_blocks[1][13], ct_blocks[11][14], ct_blocks[14][11], ct_blocks[5][8], ct_blocks[7][3], ct_blocks[11][9], ct_blocks[8][6], ct_blocks[2][15], ct_blocks[1][5], ct_blocks[7][10], ct_blocks[15][14]],
            [ct_blocks[9][7], ct_blocks[9][6], ct_blocks[7][6], ct_blocks[6][9], ct_blocks[5][2], ct_blocks[12][0], ct_blocks[6][6], ct_blocks[1][11], ct_blocks[6][0], ct_blocks[11][3], ct_blocks[14][14], ct_blocks[3][6], ct_blocks[5][15], ct_blocks[5][0], ct_blocks[8][0], ct_blocks[0][8]],
            [ct_blocks[3][0], ct_blocks[11][5], ct_blocks[5][3], ct_blocks[15][11], ct_blocks[10][4], ct_blocks[9][5], ct_blocks[15][2], ct_blocks[3][2], ct_blocks[14][3], ct_blocks[0][15], ct_blocks[3][13], ct_blocks[4][11], ct_blocks[3][5], ct_blocks[14][4], ct_blocks[9][14], ct_blocks[13][13]],
            [ct_blocks[6][8], ct_blocks[14][7], ct_blocks[13][10], ct_blocks[0][1], ct_blocks[10][5], ct_blocks[9][8], black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
            [ct_blocks[4][10], ct_blocks[1][3], ct_blocks[8][12], ct_blocks[13][9], ct_blocks[9][15], ct_blocks[0][3], ct_blocks[11][1], ct_blocks[15][9], ct_blocks[6][12], ct_blocks[11][10], ct_blocks[5][11], ct_blocks[4][12], ct_blocks[4][3], ct_blocks[0][12], ct_blocks[1][8], ct_blocks[2][0]],
            [ct_blocks[8][10], ct_blocks[9][1], ct_blocks[12][7], ct_blocks[14][0], ct_blocks[4][15], ct_blocks[15][13], ct_blocks[0][6], ct_blocks[11][0], ct_blocks[11][7], ct_blocks[10][6], ct_blocks[6][2], ct_blocks[7][13], ct_blocks[5][1], ct_blocks[2][8], ct_blocks[1][15], ct_blocks[12][13]],
            [black_block, ct_blocks[2][13], ct_blocks[8][3], ct_blocks[10][0], ct_blocks[11][11], ct_blocks[11][15], ct_blocks[6][13], ct_blocks[0][9], ct_blocks[6][5], ct_blocks[8][5], ct_blocks[1][7], ct_blocks[6][1], ct_blocks[14][15], ct_blocks[9][10], ct_blocks[13][3], ct_blocks[9][13]],
            [ct_blocks[8][13], ct_blocks[8][9], ct_blocks[8][8], ct_blocks[13][5], ct_blocks[14][1], ct_blocks[0][10], ct_blocks[0][4], ct_blocks[12][9], ct_blocks[3][12], ct_blocks[0][14], black_block, ct_blocks[8][4], ct_blocks[4][4], ct_blocks[1][2], ct_blocks[0][0], black_block],
            [ct_blocks[13][12], black_block, ct_blocks[3][3], ct_blocks[12][8], ct_blocks[12][1], ct_blocks[14][6], ct_blocks[8][2], ct_blocks[13][2], ct_blocks[2][2], ct_blocks[11][4], ct_blocks[0][2], ct_blocks[1][1], ct_blocks[15][15], ct_blocks[7][11], ct_blocks[14][9], black_block],
            [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
            [black_block, ct_blocks[14][13], ct_blocks[10][11], ct_blocks[15][10], ct_blocks[1][14], ct_blocks[13][14], ct_blocks[2][1], black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
            [black_block, ct_blocks[12][12], ct_blocks[8][1], ct_blocks[15][7], ct_blocks[7][14], ct_blocks[13][4], ct_blocks[4][7], black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
            [black_block, black_block, black_block, black_block, black_block, ct_blocks[4][5], ct_blocks[14][12], black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
            [ct_blocks[10][10], ct_blocks[10][14], ct_blocks[13][8], ct_blocks[4][1], ct_blocks[10][9], ct_blocks[1][6], ct_blocks[14][10], ct_blocks[14][2], ct_blocks[12][2], ct_blocks[10][13], ct_blocks[10][8], ct_blocks[6][11], ct_blocks[15][1], ct_blocks[15][5], ct_blocks[9][0], ct_blocks[4][6]]]

for i in range(16):
    for j in range(16):
        block = pt_blocks[i][j]
        if block != black_block:
            pos = list_blocks.index(block)
            list_blocks.pop(pos)
        
# start = ct_blocks[7][6]
# list_blocks.pop(list_blocks.index(start))
# pt_blocks[0][0] = start

def distance(tup1, tup2):
    return sum([math.exp(abs(tup1[i] - tup2[i])) for i in range(len(tup1))])

def blocks_compare_lr(b1_, b2_):
    # print('b1 :', type(b1_))
    # print('b2 :', type(b2_))
    height = b1_.size[1]
    length = b1_.size[0]
    x1, x2 = length - 1, 0
    ind = 0
    for y in range(height):
        # print('b1 : ', b1_)
        # print('b2 : ', b2_)
        t1 = b1_.getpixel((x1, y))
        t2 = b2_.getpixel((x2, y))
        ind += distance(t1, t2)
    return ind

def next_right(block_left, list_blocks_):
    index_neightboor = blocks_compare_lr(block_left, list_blocks_[0])
    nn = 0
    neightboor = list_blocks_[0]
    for n in range(1, len(list_blocks_)):
        block_right = list_blocks[n]
        ii = blocks_compare_lr(block_left, block_right)
        if ii < index_neightboor:
            index_neightboor = ii
            neightboor = block_right
            nn = n
#     if index_neightboor > 240:
#         neightboor = default_block
    return neightboor, index_neightboor, nn

def blocks_compare_ud(b1_, b2_):
    # print('b1 :', type(b1_))
    # print('b2 :', type(b2_))
    height = b1_.size[1]
    length = b1_.size[0]
    y1, y2 = height - 1, 0
    ind = 0
    for x in range(height):
        # print('b1 : ', b1_)
        # print('b2 : ', b2_)
        t1 = b1_.getpixel((x, y1))
        t2 = b2_.getpixel((x, y2))
        ind += distance(t1, t2)
    return ind

def next_down(block_up, list_blocks_):
    # print('block_up:', block_up)
    index_neightboor = blocks_compare_ud(block_up, list_blocks_[0])
    nn = 0
    neightboor = list_blocks_[0]
    for n in range(1, len(list_blocks_)):
        block_down = list_blocks[n]
        ii = blocks_compare_ud(block_up, block_down)
        if ii < index_neightboor:
            index_neightboor = ii
            neightboor = block_down
            nn = n
#     if index_neightboor > 240:
#         neightboor = default_block
    return neightboor, index_neightboor, nn

for i in range(num_hei):
    # print('i = ',i)
    if i != num_hei - 1:
        # print('pt_blocks i 0 :', pt_blocks[i][0])
        if pt_blocks[i + 1][0] == black_block:
            block_found, lost, p = next_down(pt_blocks[i][0], list_blocks)
            pt_blocks[i + 1][0] = block_found
            list_blocks.pop(p)
    for j in range(num_len - 1):
        # print('j = ', j)
        if pt_blocks[i][j + 1] == black_block:
            block_found1, diff1, p1 = next_right(pt_blocks[i][j], list_blocks)
            if i != 0:
                 block_found2, diff2, p2 = next_down(pt_blocks[i - 1][j + 1], list_blocks)
                 if diff1 > diff2:
                     block_found = block_found2
                     p = p2
                 else:
                    block_found = block_found1
                    p = p1
            else:
                block_found = block_found1
                p = p1
            pt_blocks[i][j + 1] = block_found
            list_blocks.pop(p)
        



# pt_blocks = [[ct_blocks[7][4], ct_blocks[5][6], ct_blocks[1][3], ct_blocks[7][3], ct_blocks[1][7], ct_blocks[4][1], ct_blocks[6][2], ct_blocks[2][5]],
#             [ct_blocks[4][5], ct_blocks[7][0], ct_blocks[2][0], ct_blocks[1][4], ct_blocks[5][7], ct_blocks[4][6], ct_blocks[2][6], ct_blocks[4][0]],
#             [ct_blocks[4][2], ct_blocks[5][1], ct_blocks[3][5], ct_blocks[6][7], ct_blocks[4][3], ct_blocks[6][6], ct_blocks[1][2], ct_blocks[6][3]],
#             [ct_blocks[6][1], ct_blocks[4][7], ct_blocks[1][0], ct_blocks[2][7], ct_blocks[1][5], ct_blocks[0][1], ct_blocks[2][4], ct_blocks[0][6]],
#             [ct_blocks[3][7], ct_blocks[0][5], ct_blocks[0][4], ct_blocks[2][1], ct_blocks[6][4], ct_blocks[5][0], ct_blocks[5][5], ct_blocks[7][1]],
#             [ct_blocks[0][7], ct_blocks[3][2], ct_blocks[3][3], ct_blocks[0][2], ct_blocks[7][7], ct_blocks[0][0], ct_blocks[2][3], ct_blocks[7][6]],
#             [ct_blocks[5][2], ct_blocks[6][0], ct_blocks[6][5], ct_blocks[5][3], ct_blocks[2][2], ct_blocks[7][5], ct_blocks[1][6], ct_blocks[3][1]],
#             [ct_blocks[4][4], ct_blocks[5][4], ct_blocks[3][4], ct_blocks[7][2], ct_blocks[3][6], ct_blocks[0][3], ct_blocks[1][1], ct_blocks[3][0]]]

# rest_blocks = [[black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
#                [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
#                [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
#                [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
#                [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
#                [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
#                [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
#                [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block]]


def cherche(b):
    global ct_blocks
    for i in range(len(ct_blocks)):
        if b in ct_blocks[i]:
            j = ct_blocks[i].index(b)
            return (i, j)
    return (-1, -1)
        
        
solution = [[None for j in range(num_hei)] for i in range(num_len)]

for i in range(num_len):
    for j in range(num_hei):
        block = pt_blocks[i][j]
        pos = cherche(block)
        solution[i][j] = pos
        
for i in range(len(solution)):
    print(solution[i])

pt_image = Image.new('RGB', ct_image.size)
for i in range(num_len):
    for j in range(num_hei):
        block = pt_blocks[i][j]
        for l in range(block_size_len):
            for h in range(block_size_hei):
                coord = (l, h)
                (r, g, b) = block.getpixel(coord)
                pt_image.putpixel((j * block_size_len + l, i * block_size_hei + h), (r, g, b))

# rest_image = Image.new('RGB', ct_image.size)
# for i in range(num_len):
#     for j in range(num_hei):
#         block = rest_blocks[i][j]
#         for l in range(block_size_len):
#             for h in range(block_size_hei):
#                 coord = (l, h)
#                 (r, g, b) = block.getpixel(coord)
#                 rest_image.putpixel((j * block_size_len + l, i * block_size_hei + h), (r, g, b))
# 
# rest_image.save('puzzle-trouble-hard_rest.jpg')
pt_image.save('puzzle-trouble-hard_solution.jpg')
