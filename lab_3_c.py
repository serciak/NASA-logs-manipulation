from util import lab_3_c_util as l3c

if __name__ == '__main__':
    biggest_asset = l3c.get_biggest_asset()
    print('Path: ', biggest_asset.group(4), ' Size: ', biggest_asset.group(6))
