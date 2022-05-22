fx6 = {'uhd_xavc-i_422_10_50': 500,
       'uhd_xavc-i_422_10_25': 250,
       'hd_xavc-i_422_10_50': 222,
       'hd_xavc-i_422_10_25': 112}


def get_bitrate():
    index = f"uhd_xavc-i_422_10_50"
    bitrate = fx6[index]
    return bitrate


cam_list = [fx6]

print(get_bitrate())