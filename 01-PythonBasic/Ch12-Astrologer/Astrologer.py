
def get_birthday_dict(year=1900, month=1, day=1) -> dict:
    """
    會回傳一個dict，dict儲存生日中每個數字的數量。
    ex 1995 12 13 -> 1有3個 2有1個 3有1個 5有1個 9有2個
    這樣回傳
    {
        1:3,
        2:1,
        3:1,
        5:1,
        9:2
    }
    """
    return {
        1: 3,
        2: 1,
        3: 1,
        5: 1,
        9: 2
    }


def get_life_number(year=1900, month=1, day=1) -> int:
    """
    會回傳一個生命靈數，生命靈數的計算方式是出生年月日的每一個數字的總和，不斷加總至個位數。
    ex 1995 12 13 -> 1+9+9+5+1+2+1+3 = 31 -> 3+1 =4
    ex 1993 8 15 -> 1+9+9+3+8+1+5 = 36 -> 3+6 =9
    這樣生命靈數就是4
    """
    return 4


def get_constellation(month, day) -> str:
    """
    根據生日回傳正確的星座
    牡羊座	3月21日～4月20日
    金牛座	4月21日～5月20日
    雙子座	5月21日～6月20日
    巨蟹座	6月21日～7月22日
    獅子座	7月23日～8月22日
    處女座	8月23日～9月22日
    天秤座	9月23日～10月22日
    天蠍座	10月23日～11月22日
    射手座	11月23日～12月22日
    魔羯座	12月23日～1月21日
    水瓶座	1月22日～2月19日
    雙魚座	2月20日～3月20日
    """
    return "水瓶座"