import urllib3
import json
import datetime
import os

def lambda_handler(event, context):
  url = 'https://slack.com/api/'
  token = os.getenv("SLACK_TOKEN")
  # botを除外するために収集したい人のreal_nameを設定しておく必要あり
  real_names = {'Taro Yamada', 'Jiro Tanaka', 'Saburo Sato'}

  http = urllib3.PoolManager()
  res = http.request('GET',url+'users.list',fields={'token':token}).data.decode()
  users = json.loads(res)['members']

  statuses = dict()
  for uinfo in users:
    if uinfo['profile']['real_name'] in real_names:
      res = http.request('GET',url+'users.getPresence',fields={'token':token, 'user':uinfo['id']}).data.decode()
      status = json.loads(res)
      statuses[uinfo['profile']['real_name']] = status['presence']

  dt_now_jst = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
  ret = {'time': dt_now_jst.strftime('%m/%d %H:%M'), 'statuses': statuses}
  return ret

if __name__ == '__main__':
  print(lambda_handler('',''))
