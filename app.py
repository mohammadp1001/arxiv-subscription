
from datetime import datetime
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import models
import crud 


s = crud.Session()

app = Flask(__name__)
@app.route("/",methods = ['GET', 'POST'])

def index():
    
    if request.method == 'POST':
    
        email,keywords,categories = new_user()
        user = models.data_user(KEYWORDS=keywords,EMAIL=email,CATEGORIES=categories)
        s.add(user)
        s.commit()     
        s.close_all()
        
    return render_template('index.html')


def new_user():
      
       data_usr = request.form.to_dict()
       email = data_usr["email"]
       keywords = data_usr["keywords"]
       categories = ""
       if "phys" in data_usr:
            phys = data_usr["phys"]
            categories = categories + phys + ","
       if "cs" in data_usr:
            cs = data_usr["cs"]
            categories = categories + cs + ","
       if "math" in data_usr:     
            math = data_usr["math"]
            categories = categories + math + ","
       if "st" in data_usr:
            st = data_usr["st"]
            categories = categories + st + ","
       if "qf" in data_usr:     
            qf = data_usr["qf"]
            categories = categories + qf + ","
            
       return email,keywords,categories
       
if __name__ == "__main__":
    app.run(debug=True)
