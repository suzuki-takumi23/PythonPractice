#datetimeモジュールをインポート
import datetime

#変数todayを宣言
#datetimeモジュールのdateクラスにあるtoday関数を使う
#戻り値をtodayに代入
today = datetime.date.today()

#変数todyadetailを宣言
#datetimeモジュールのdatetimeクラスにあるtoday関数を使います
#todaydetailに代入
todaydetail = datetime.datetime.today()

#今日の日付
print('----------------------------------------')
print(today)
print(todaydetail)

#それぞれの値を別で取り出すことも可能
print('----------------------------------------')

#年を出力(yearプロパティ)
print(today.year)
#月を出力(monthプロパティ)
print(today.month)
#日を出力(dayプロパティ)
print(today.day)

#todaydetail
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
#時間を出力(hourプロパティ)
print(todaydetail.hour)
#分を出力(minuteプロパティ)
print(todaydetail.minute)
#秒を出力(secondプロパティ)
print(todaydetail.second)
#ミリ秒を出力(microsecondプロパティ)
print(todaydetail.microsecond)

#日付のフォーマット
print('------------------------------------------')
print(today.isoformat())
print(todaydetail.strftime("%Y/%m/%d %H:%M:%S"))