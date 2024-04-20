import pyDigitalWaveTools.vcd.parser as pwt_vcd_parser
import json

# https://github.com/Nic30/pyDigitalWaveTools
# https://pydigitalwavetools.readthedocs.io/en/latest/pyDigitalWaveTools.vcd.html -> assez imbuvable

def read_vcd(src):
    with open(src) as vcd_file:
        vcd = pwt_vcd_parser.VcdParser()
        vcd.parse(vcd_file)
        d = vcd.scope.toJson()
    return d


if __name__ == '__main__':
    file_name = 'very-cute-data.vcd'
    datas = read_vcd(file_name)
              
#     f = open('test.txt', 'w')
#     f.write(json.dumps(datas, indent=4, sort_keys=True))
#     f.close()
    
    children_children = datas['children'][0]['children']
    d0_datas = children_children[0]['data']
    d1_datas = children_children[1]['data']
    intervall = [(0, 350000), (350000, 2000000)]
    start, end = intervall [1]
    #rep = '1000100010'
    
    sol = 'FCSC{'
    timestamp_d0, pos_d0 = d0_datas.pop(0)
    timestamp_d1, pos_d1 = d1_datas.pop(0)
    continuer = True
    intervall_ok = (start <= timestamp_d1)
    while continuer:
        new_timestamp_d1, new_pos_d1 = d1_datas.pop(0)
        if (start <= new_timestamp_d1 <= end) and (pos_d1 =='1') and (new_pos_d1 == '0'):
            found = False
            #print(new_timestamp_d1)
            while not found:
                if new_timestamp_d1 < d0_datas[0][0]:
                    sol += pos_d0
                    found = True
                else:
                    timestamp_d0, pos_d0 = d0_datas.pop(0)
        timestamp_d1, pos_d1 = new_timestamp_d1, new_pos_d1
        if timestamp_d1 >= end:
            sol = sol + '}'
            continuer = False
    print(sol)