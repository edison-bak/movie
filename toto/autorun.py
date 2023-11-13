

from django_cron import CronJobBase, Schedule
from .data import *

class YourCronJob(CronJobBase):
    RUN_EVERY_MINS = 24 * 60  # 24시간에 한 번 실행
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'yourapp.your_cron_job'  # 임의의 코드 이름

    def do(self):
        api_key = 'cb276b669f6f4e9cb0ad5c32a78ec0d7'
        df = get_matches_data(api_key)
        update_and_upload_data(df)