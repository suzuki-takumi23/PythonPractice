import datetime
#メンバ関数を定義
def get_today():

    today = datetime.datetime.today()
    
    #タプル(配列)は()
    value = (today.year, today.month, today.day)
    
    return value
#関数を使用
test_tuple = get_today()

print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])