import requests

a=8950
while a < 10000:
 data = requests.post("https://www.bt.cn/api/group_activity/add_team_order", data={
"activity_id": 6,
"tid": a
}, cookies={
"PHPSESSID": "改成自己的"
})
 print(data.text)
 a=a+1
