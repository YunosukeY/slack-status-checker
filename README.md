# Slack Status Checker
Slackメンバーのログイン具合を可視化します．

## 使ったもの
- Slack API
- AWS
  - S3: Lambda Layer用
  - Lambda
  - EventBridge: トリガー
  - SQS: データを貯める用 

## ファイル
### status_collector.py
メンバーのステータスを収集します．

### status_visualizer.py
収集したデータをグラフにし，Slackに送ります．

## 参考文献
https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/lambda-python.html  
https://www.suzu6.net/posts/136-lambda-cron-rate/  
https://docs.aws.amazon.com/ja_jp/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-create-queue.html  
https://docs.aws.amazon.com/ja_jp/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-add-permissions.html  
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_Operations.html

https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html  
https://dev.classmethod.jp/articles/boto3_sqs_lambda_schedule_trial/  
https://qiita.com/tottu22/items/594e8c506ece0f8cc87c  
https://qiita.com/hoto17296/items/a374efc2d8159d75bc71