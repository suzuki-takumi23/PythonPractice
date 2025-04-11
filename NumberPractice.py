test_integer = 100

print(test_integer + 10)    #加算
print(test_integer - 10)    #減算
print(test_integer * 10)    #乗算
print(test_integer / 10)    #除算

test_str = '100'

#数値への変換
print(int(test_str) + 100)

#浮動小数点数はfloatを使います
test_str = '100.5'
print(float(test_str) + 100)

#整数部が０の時は整数部を省略できます
test_float = .5
print(test_float)

#複素数を表すcomplexは数値にjやJを付与します
test_complex = 100 + 5j

print(test_complex)
print(test_complex.real)
print(test_complex.imag)