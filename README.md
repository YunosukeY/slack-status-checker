# Slack Status Checker
Slackメンバーのログイン具合を可視化します．

![使用イメージ](https://user-images.githubusercontent.com/39757050/84554370-7def9c00-ad52-11ea-928f-c3594ca04133.png)

## 構成
![構成図](https://user-images.githubusercontent.com/39757050/84477914-6a4d2280-accb-11ea-8b5a-be86c542c781.png)

## ファイル
### status_collector.py
メンバーのステータスを収集します．  
Lambdaでは一定時間おきに実行し，結果をSQSに貯めます．

### status_visualizer.py
収集したデータをグラフにし，結果をSlackにアップロードします．  
Lambdaでは1日おきに実行します．

## 参考文献
[LambdaのPythonチュートリアル](https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/lambda-python.html)  
[Lambdaで定期処理](https://www.suzu6.net/posts/136-lambda-cron-rate/)  
[SQSチュートリアル](https://docs.aws.amazon.com/ja_jp/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-create-queue.html)  
[SQSのアクセス制限追加](https://docs.aws.amazon.com/ja_jp/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-add-permissions.html)  
[SQSアクション一覧](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_Operations.html)

[SQSからの受信](https://dev.classmethod.jp/articles/boto3_sqs_lambda_schedule_trial/)  
[Slackに画像をアップロードする](https://qiita.com/tottu22/items/594e8c506ece0f8cc87c)  
[LambdaのLayer作成](https://qiita.com/hoto17296/items/a374efc2d8159d75bc71)
