from project import days_until_today,convert_jalali,convert_Gregorian

def test_1():
    assert days_until_today(2000, 2, 17) == 8715
    assert days_until_today(2002, 7, 15) == 7836
    assert days_until_today(2002, 15, 15) == "False"
    assert days_until_today(2002, "gh", 15) == "False"

def test_2():
    assert convert_jalali(1399, 1, 5) == "2020/3/24"
    assert convert_jalali(1187, 11, 23) == "1809/2/12"  #Darvin birthday
    assert convert_jalali(1378, 11, 22) == "2000/2/11"
    assert convert_jalali(1381, 4, "24") == "False"

def test_3():
    assert convert_Gregorian(2002, 7, 15) == "1381/04/24"
    assert convert_Gregorian(1809, 2, 12) == "1187/11/23"
    assert convert_Gregorian(2002, "7", 15) == "False"
    assert convert_Gregorian(2200, 75, 15) == "False"
