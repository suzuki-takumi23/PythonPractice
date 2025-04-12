#リストは[]で囲います
test_list1 = ['python', '-', 'izm', '.', 'com']
print(test_list1)

print('---------------------------------------------')

for i in test_list1:
    print(i)

test_list_1 = []
print(test_list_1)

print('---------------------------------------------')

#要素の追加はappendを使います
test_list_1.append('python')
test_list_1.append('-')
test_list_1.append('izm')
test_list_1.append('.')
test_list_1.append('com')

print(test_list_1)

test_list_2 = ['python', 'izm', 'com']
print(test_list_2)

print('----------------------------------------------')

#要素番号を指定するときはinsertを使います
test_list_2.insert(1, '-')
test_list_2.insert(3, '.')

print(test_list_2)

test_list_2.insert(0, 'http://www.')

print(test_list_2)

#要素の削除はremoveを使います
test_list_3 = ['1', '2', '3', '2', '1']
print(test_list_3)

print('-----------------------------------------------')

test_list_3.remove('2')

print(test_list_3)

test_list_3 = ['1', '2', '3', '2', '1']
print(test_list_3)

print('-------------------------------------------------')

#要素番号を参照して削除する場合はpopを使用します
print(test_list_3.pop(1))
print(test_list_3)

#引数なしで使用すると削除されます
print(test_list_3.pop())
print(test_list_3)

#要素のインデックス番号を取得するにはindexを使います
test_list_4 = ['100', '200', '300', '200', '100']

print(test_list_4.index('200'))

#count引数の要素がリスト内にいくつあるかを返します
test_list_5 = ['100', '200', '300', '200', '100']
print(test_list_5.count('200'))