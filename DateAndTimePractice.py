#datetimeモジュールをインポート
import datetime
import calendar

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

#日付の計算
today = datetime.datetime.today()

#今日の日付
print(today)

#明日の日付
print(today + datetime.timedelta(days=1))

newyear = datetime.datetime(2010, 1, 1)

#2010年1月1日の一週間後
print(newyear + datetime.timedelta(days=7))

#2010年1月1日から今日までの日数
calc = today - newyear

#計算結果の戻り値はtimedelta
print(calc.days)

print(calendar.isleap(2015))
print(calendar.isleap(2016))
print(calendar.isleap(2017))

print(calendar.leapdays(2010, 2020))