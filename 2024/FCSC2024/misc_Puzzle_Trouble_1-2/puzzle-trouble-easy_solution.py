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

black_block = Image.new('RGB', (block_size_len, block_size_hei))

pt_blocks = [[ct_blocks[7][4], ct_blocks[5][6], ct_blocks[1][3], ct_blocks[7][3], ct_blocks[1][7], ct_blocks[4][1], ct_blocks[6][2], ct_blocks[2][5]],
            [ct_blocks[4][5], ct_blocks[7][0], ct_blocks[2][0], ct_blocks[1][4], ct_blocks[5][7], ct_blocks[4][6], ct_blocks[2][6], ct_blocks[4][0]],
            [ct_blocks[4][2], ct_blocks[5][1], ct_blocks[3][5], ct_blocks[6][7], ct_blocks[4][3], ct_blocks[6][6], ct_blocks[1][2], ct_blocks[6][3]],
            [ct_blocks[6][1], ct_blocks[4][7], ct_blocks[1][0], ct_blocks[2][7], ct_blocks[1][5], ct_blocks[0][1], ct_blocks[2][4], ct_blocks[0][6]],
            [ct_blocks[3][7], ct_blocks[0][5], ct_blocks[0][4], ct_blocks[2][1], ct_blocks[6][4], ct_blocks[5][0], ct_blocks[5][5], ct_blocks[7][1]],
            [ct_blocks[0][7], ct_blocks[3][2], ct_blocks[3][3], ct_blocks[0][2], ct_blocks[7][7], ct_blocks[0][0], ct_blocks[2][3], ct_blocks[7][6]],
            [ct_blocks[5][2], ct_blocks[6][0], ct_blocks[6][5], ct_blocks[5][3], ct_blocks[2][2], ct_blocks[7][5], ct_blocks[1][6], ct_blocks[3][1]],
            [ct_blocks[4][4], ct_blocks[5][4], ct_blocks[3][4], ct_blocks[7][2], ct_blocks[3][6], ct_blocks[0][3], ct_blocks[1][1], ct_blocks[3][0]]]

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