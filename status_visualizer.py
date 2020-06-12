import boto3
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import io
import datetime
import os

# 06/11 20:30 -> 20.5
def extract_hors(s):
  return int(s[6:8])+int(s[9:])/60.0

def count_active(m):
  c = 0
  for k, v in m.items():
    if v == 'active':
      c += 1
  return c

# SQSのデータを取り出す
def get_data():
  name = 'slack-statuses'
  sqs = boto3.resource('sqs',region_name='ap-northeast-1')
  queue = sqs.get_queue_by_name(QueueName=name)
  
  res = []
  while len(res) < 24:
    msg_list = queue.receive_messages(MaxNumberOfMessages=10)
    if msg_list:
      res.extend(msg_list)
  return res

# 時間毎のactive人数を集計
def aggregate(msg_list):
  left = []
  height = []
  for message in msg_list:
    m = json.loads(message.body)['responsePayload']
    left.append(extract_hors(m['time']))
    height.append(count_active(m['statuses']))
    message.delete()
  df = pd.DataFrame({'hour': left, 'number': height})
  return df

def jst_now():
  return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))

def plot(df):
  sns.set()
  sns.lineplot(x="hour", y="number", data=df)
  plt.title(jst_now().strftime('%m/%d'))
  plt.xlim(0,24)
  plt.ylim(0,20)

def send():
  # Lambdaでは保存できないのでBytesIOにした後BufferedReaderにする 
  item = io.BytesIO()
  plt.savefig(item, format='png')
  item.seek(0)

  token = os.getenv("SLACK_TOKEN")
  channel = os.getenv("SLACK_DM_ID")
  url = 'https://slack.com/api/'
  files = {'file': io.BufferedReader(item)}
  now = jst_now()
  param = {
    'token':token, 
    'channels':channel,
    'filename':now.strftime('%m%d.png'),
    'title':now.strftime('%m/%dの結果です')
    
  }
  requests.post(url=url+'files.upload',params=param, files=files)

def lambda_handler(event, context):
  msg_list = get_data()
  df = aggregate(msg_list)
  plot(df)
  send()
