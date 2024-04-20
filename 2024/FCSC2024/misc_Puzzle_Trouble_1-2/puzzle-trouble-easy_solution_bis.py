from PIL import Image
import numpy

ct_image = Image.open('puzzle-trouble-easy.jpg')

assert ct_image.format == 'JPEG'
assert ct_image.mode == 'RGB'

ct_length, ct_height = ct_image.size
assert ct_image.size == (1024, 1024)

num_len = 8
block_size_len = ct_length // num_len # Number of blocks on the length
num_hei = 8
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

pt_blocks = [[black_block for j in range(num_len)] for i in range(num_hei)]

start = ct_blocks[7][4]
list_blocks.pop(list_blocks.index(start))
pt_blocks[0][0] = start

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
        (r1, g1, b1) = b1_.getpixel((x1, y))
        (r2, g2, b2) = b2_.getpixel((x2, y))
        ind += abs(r2 - r1) + abs(g2 - g1) + abs(b2 - b1)
    return ind

def next_right(block_left, list_blocks_, default_block):
    index_neightboor = blocks_compare_lr(block_left, list_blocks_[0])
    neightboor = default_block
    for block_right in list_blocks_:
        ii = blocks_compare_lr(block_left, block_right)
        if ii < index_neightboor:
            index_neightboor = ii
            neightboor = block_right
#     if index_neightboor > 240:
#         neightboor = default_block
    return neightboor, index_neightboor

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
        (r1, g1, b1) = b1_.getpixel((x, y1))
        (r2, g2, b2) = b2_.getpixel((x, y2))
        ind += abs(r2 - r1) + abs(g2 - g1) + abs(b2 - b1)
    return ind

def next_down(block_up, list_blocks_, default_block):
    # print('block_up:', block_up)
    index_neightboor = blocks_compare_ud(block_up, list_blocks_[0])
    neightboor = default_block
    for block_down in list_blocks_:
        ii = blocks_compare_ud(block_up, block_down)
        if ii < index_neightboor:
            index_neightboor = ii
            neightboor = block_down
#     if index_neightboor > 240:
#         neightboor = default_block
    return neightboor, index_neightboor

for i in range(num_hei):
    # print('i = ',i)
    if i != num_hei - 1:
        # print('pt_blocks i 0 :', pt_blocks[i][0])
        block_found, lost = next_down(pt_blocks[i][0], list_blocks, black_block)
        pt_blocks[i + 1][0] = block_found
        if block_found in list_blocks:
            list_blocks.pop(list_blocks.index(block_found))
    for j in range(num_len - 1):
        # print('j = ', j)
        block_found1, diff1 = next_right(pt_blocks[i][j], list_blocks, black_block)
        if i != 0:
            block_found2, diff2 = next_down(pt_blocks[i - 1][j + 1], list_blocks, black_block)
            if False:#diff1 > diff2:
                block_found = block_found2
            else:
                block_found = block_found1
        else:
            block_found = block_found1
        pt_blocks[i][j + 1] = block_found1
        if block_found in list_blocks:
            list_blocks.pop(list_blocks.index(block_found))
        



# pt_blocks = [[ct_blocks[7][4], ct_blocks[5][6], ct_blocks[1][3], ct_blocks[7][3], ct_blocks[1][7], ct_blocks[4][1], ct_blocks[6][2], ct_blocks[2][5]],
#             [ct_blocks[4][5], ct_blocks[7][0], ct_blocks[2][0], ct_blocks[1][4], ct_blocks[5][7], ct_blocks[4][6], ct_blocks[2][6], ct_blocks[4][0]],
#             [ct_blocks[4][2], ct_blocks[5][1], ct_blocks[3][5], ct_blocks[6][7], ct_blocks[4][3], ct_blocks[6][6], ct_blocks[1][2], ct_blocks[6][3]],
#             [ct_blocks[6][1], ct_blocks[4][7], ct_blocks[1][0], ct_blocks[2][7], ct_blocks[1][5], ct_blocks[0][1], ct_blocks[2][4], ct_blocks[0][6]],
#             [ct_blocks[3][7], ct_blocks[0][5], ct_blocks[0][4], ct_blocks[2][1], ct_blocks[6][4], ct_blocks[5][0], ct_blocks[5][5], ct_blocks[7][1]],
#             [ct_blocks[0][7], ct_blocks[3][2], ct_blocks[3][3], ct_blocks[0][2], ct_blocks[7][7], ct_blocks[0][0], ct_blocks[2][3], ct_blocks[7][6]],
#             [ct_blocks[5][2], ct_blocks[6][0], ct_blocks[6][5], ct_blocks[5][3], ct_blocks[2][2], ct_blocks[7][5], ct_blocks[1][6], ct_blocks[3][1]],
#             [ct_blocks[4][4], ct_blocks[5][4], ct_blocks[3][4], ct_blocks[7][2], ct_blocks[3][6], ct_blocks[0][3], ct_blocks[1][1], ct_blocks[3][0]]]

rest_blocks = [[black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
               [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
               [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
               [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
               [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
               [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
               [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block],
               [black_block, black_block, black_block, black_block, black_block, black_block, black_block, black_block]]

pt_image = Image.new('RGB', ct_image.size)
for i in range(num_len):
    for j in range(num_hei):
        block = pt_blocks[i][j]
        for l in range(block_size_len):
            for h in range(block_size_hei):
                coord = (l, h)
                (r, g, b) = block.getpixel(coord)
                pt_image.putpixel((j * block_size_len + l, i * block_size_hei + h), (r, g, b))

rest_image = Image.new('RGB', ct_image.size)
for i in range(num_len):
    for j in range(num_hei):
        block = rest_blocks[i][j]
        for l in range(block_size_len):
            for h in range(block_size_hei):
                coord = (l, h)
                (r, g, b) = block.getpixel(coord)
                rest_image.putpixel((j * block_size_len + l, i * block_size_hei + h), (r, g, b))

rest_image.save('puzzle-trouble-easy_rest.jpg')
pt_image.save('puzzle-trouble-easy_solution.jpg')