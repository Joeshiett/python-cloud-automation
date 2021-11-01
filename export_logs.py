import boto3
import collections
from datetime import datetime, date, time, timedelta

region = 'eu-west-1'

def lambda_handler(event, context):
    yesterday = datetime.combine(date.today()-timedelta(1),time())
    today = datetime.combine(date.today(),time())
    unix_start = datetime(1970,1,1)
    client = boto3.client('logs')
    response = client.create_export_task(
        taskName='Export_CloudwatchLogs',
        logGroupName='/var/log/syslog',
        fromTime=int((yesterday-unix_start).total_seconds() * 1000),
        to=int((today -unix_start).total_seconds() * 1000),
        destination='joeshiett-cw-logs',
        destinationPrefix='bucket-{}'.format(yesterday.strftime("%Y-%m-%d"))
        )
    return 'Response from export task at {} :\n{}'.format(datetime.now().isoformat(),response)
