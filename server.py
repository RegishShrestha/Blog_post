from flask import Flask, render_template
import random
import datetime
app=Flask(__name__)

@app.route('/')
def home():
    random_num=random.randint(1,10)
    
    year=datetime.date.today().year
    return render_template('index.html',num=random_num,y=year)

if __name__=='__main__':
    app.run(debug=True)
    

