from datetime import date, timedelta

day_in_week = "月火水木金土日"
start = date( 2020, 11, 1 )

for d in range(31):
  cur = start + timedelta( days=d )
  wd = cur.weekday()
  if day_in_week[wd] == "日":
    print("\n")

  print(cur, day_in_week[wd])