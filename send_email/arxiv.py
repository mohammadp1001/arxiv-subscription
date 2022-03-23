import urllib, urllib.request
import feedparser

import datetime 
# cat	Subject Category
# abs	Abstract
# au	Author
# ti	Title

 
def days_between(d,date=None):
    d = datetime.datetime.strptime(d, "%Y-%m-%d")
    today = datetime.datetime.today()
    return abs((d - today).days)

def get_from_arxiv(keywords,date=None):

    ind = len(keywords)

    if len(keywords) == 1:
        s = '%28ti:'+ keywords[0]
    else:
        while ind > 0:   
            if ind == len(keywords):
                s = '%28ti:'+ keywords[ind-1] 
                ind = ind - 1        
            else:    
                s = s + '+AND+ti:'+keywords[ind-1]
                ind = ind - 1
    s = s + '%29'  
          
    all_result = []
    for i in range(1,10):
        url = 'http://export.arxiv.org/api/query?search_query='+ s + '&start='+str((i-1)*10)+'&max_results='+str(i*10)     
        url = url + '&sortBy=submittedDate&sortOrder=descending'
        data = urllib.request.urlopen(url)
        string_arxiv  = data.read()
        all_result.append(string_arxiv)
    
    
    res = ""
    for result in all_result:
        feed = feedparser.parse(result)
        for entry in feed.entries:
            if days_between(entry.published[:10]) < 14:
                res = res + "The title: " + entry.title + "\n" + "The published date: " + entry.published[:10] +"\n" + "The link: " + entry.link + "\n" 
                
    return res      
if __name__ == '__main__':    
    keywords = ['hall','thermal']
    res = get_from_arxiv(keywords)
