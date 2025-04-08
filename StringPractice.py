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

#文字列の結合はこっちでもおｋ
test_str3 = '012'
test_str3 += '345'
test_str3 += '678'
test_str3 += '9'

print(test_str3)

#文字列の繰り返しならこの表現でもおｋ
test_str4 = '012' * 3

print(test_str4)

#文字列への変換はこんな感じ
test_integer = 100
print(str(test_integer) + 'yen')

#文字列の置換にはreplaceを使います
#第一引数が変更対象、第二引数が変更後の文字列です
test_str5 = 'python-izm'
print(test_str5.replace('izm', 'ism'))

#文字列の分割にはsplitを使います
#戻り値はリストです
test_str6 = 'python-izm'
print(test_str6.split('-'))

#文字列の桁揃えはrjustを使います
#第一引数が全体の文字数、第二引数が埋め込む文字列です
test_str7 = '1234'
print(test_str7.rjust(10, '0'))
print(test_str7.rjust(10, '!'))

#特定の文字列を指定せずゼロで埋める場合はzfillを使います
test_str8 = '1234'
print(test_str8.zfill(10))
print(test_str8.zfill(3))

#文字列の戦闘が任意の文字列の時にtrueを返すstartswith
test_str9 = 'python-izm'
print(test_str9.startswith('python'))
print(test_str9.startswith('izm'))

#文字列中に任意の文字が含まれているかを調べるnin
test_str10 = 'python-izm'
print('z' in test_str10)
print('s' in test_str10)

#大文字もしくは小文字に変換するupper,lower
test_str11 = 'Python-Izm.Com'
print(test_str11.upper())
print(test_str11.lower())

#文字列の先頭、末尾を削除するときはlstrip,rstripを使います
print('-------------------------------------------')
test_str12 = '         python-izm.com'
print(test_str12)

test_str12 = test_str12.lstrip()
print(test_str12)

test_str12 = test_str12.lstrip('python')
print(test_str12)

print('-------------------------------------------')
test_str13 = 'python-izm.com           '
print(test_str13 + '/')

test_str13 = test_str13.rstrip()
print(test_str13 + '/')

test_str13 = test_str13.rstrip('com')
print(test_str13)
