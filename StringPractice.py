#文字列はシングルクォーテーションでも
#ダブルクォーテーションでも囲えます
print('python-izm')
print("python-izm")

#ダブルクォーテーション三つで囲むと改行にも対応します
test_str = """
test1
test2
"""
print(test_str)

#文字列の結合は算術演算子でできます。
test_str2 = 'python'
test_str2 = test_str2 + '_'
test_str2 = test_str2 + 'izm'

print(test_str2)

#
test_str3 = '012'
test_str3 += '345'
test_str3 += '678'
test_str3 += '9'

print(test_str3)

test_str4 = '012' * 3

print(test_str4)

test_integer = 100
print(str(test_integer) + 'yen')

