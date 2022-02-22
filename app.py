import streamlit as st

guaranteed_jewel = 30000

def calc_jewel(jewel, ticket, times, guaranteed_cnt):
    gacha_cnt = jewel + ticket * 150
    need_jewel = guaranteed_jewel * guaranteed_cnt - gacha_cnt
    '必要なジュエルの数：', need_jewel
    # print('必要なジュエルの数：', need_jewel)
    get_jewel_sum = 0
    need_money_dict = {10000: 0, 5020: 0, 3060: 0, 1480: 0, 730: 0, 370: 0, 120: 0}
    while need_jewel > 0:
        if need_jewel > 2500:
            if times:
                get_jewel = 7500
                need_money_dict[10000] += 1
            else:
                get_jewel = 5000
                need_money_dict[10000] += 1
        elif need_jewel > 1500:
            get_jewel = 2500
            need_money_dict[5020] += 1
        elif need_jewel > 700:
            get_jewel = 1500
            need_money_dict[3060] += 1
        elif need_jewel > 320:
            get_jewel = 700
            need_money_dict[1480] += 1
        elif need_jewel > 160:
            get_jewel = 320
            need_money_dict[730] += 1
        elif need_jewel > 50:
            get_jewel = 160
            need_money_dict[370] += 1
        else:
            get_jewel = 50
            need_money_dict[120] += 1
        need_jewel -= get_jewel
        get_jewel_sum += get_jewel

    need_money = 0
    for key, value in need_money_dict.items():
        print(f'{key}円を{value}回。')
        need_money += key * value
    '必要な金額：', need_money
    '得られるジュエルの数：', get_jewel_sum
    # print('必要な金額：', need_money)
    # print('得られるジュエルの数：', get_jewel_sum)

def main():
    # jewel = 9170
    # ticket = 0
    # times = 0
    # guaranteed_cnt = 0

    st.title('課金額計算ツール')
    st.header('概要')
    st.write('財産を入力してください。目標到達度と必要課金額を算出します。')
    jewel = st.number_input('ジュエルの数', value=0)
    ticket = st.number_input('チケットの数', value=0)
    times = st.number_input('安いやつの残り', value=0)
    guaranteed_cnt = st.number_input('天井する回数', value=0)
    # mode = st.selectbox('算出モード設定', ['1万円単位', '最安値'])
    # '算出モード：', mode

    calc_jewel(jewel, ticket, times, guaranteed_cnt)

if __name__ == '__main__':
    main()