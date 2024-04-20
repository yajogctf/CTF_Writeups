for i in range(16):
    lig = ''
    lig += '['
    for j in range(16):
        lig += 'ct_blocks[' + str(i) + '][' + str(j) + ']'
        if j != 15:
            lig += ','
        else:
            lig += '],'
    print(lig)

for i in range(16):
    lig = '['
    for j in range(16):
        lig += 'black_block'
        if j != 15:
            lig += ', '
        else:
            lig += '],'
    print(lig)