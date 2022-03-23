from apscheduler.schedulers.blocking import BlockingScheduler
import arxiv
import func
import crud

#https://levelup.gitconnected.com/automate-sending-daily-mails-using-python-952ede021422
sched = BlockingScheduler()



@sched.scheduled_job('cron', day_of_week='fri',hour = 8)
def scheduled_job():
    print('This job is run every week Friday at 8 AM.')
    _keywords,_emails = func.fetch_user_data(crud.engine)
    for count,value in enumerate(zip(_emails,_keywords)):
        text = arxiv.get_from_arxiv(value[1].split(","),date=None)    
        func.send_email(value[0], "The new articles from arxiv.", text)

sched.start()


