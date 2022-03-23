
import smtplib, ssl
import config
import arxiv
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart







#https://github.com/Kakarot-2000/Daily-Puzzle   
#https://docs.python.org/2/library/email-examples.html#id5

def fetch_user_data(engine):
    
    conn = engine.connect()
    df = pd.read_sql_table('users', conn)

    return df["KEYWORDS"].tolist(),df["EMAIL"].tolist()
         
def send_email(recipient, subject, body):

                    
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = config.GMAIL_USER
    message["To"] = recipient
   
    part = MIMEText(body, "plain")
    message.attach(part)


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(config.GMAIL_USER, config.GMAIL_PASSWORD)
        server.sendmail(
            config.GMAIL_USER, recipient, message.as_string()
            )   
         
    
    
    
    
if __name__ == '__main__':
    keywords = ['hall','thermal']
    text = arxiv.get_from_arxiv(keywords,date=None)
    send_email("mohammad.p69@gmail.com", "The new articles", text)
 