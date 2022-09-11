import requests
import random
import datetime
from bs4 import BeautifulSoup
from flask import Flask, render_template


app=Flask(__name__)
@app.route('/')
def home():
    random_num=random.randint(1,10)
    year=datetime.date.today().year
    return render_template('index.html',num=random_num,y=year)

@app.route('/guess/<name>/')
def guess(name):
    gender_url=f'https://api.genderize.io?name={name}'
    gender_response=requests.get(gender_url)
    gender_json=gender_response.json()
    gender=gender_json['gender']
    age_response=requests.get(f'https://api.agify.io?name={name}')
    age_json=age_response.json()
    age=age_json['age']
    
    return render_template('guess.html',name=name,gender=gender,age=age)

@app.route('/blog')
def blog():
    blog_data=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    allblog=blog_data.json()
    return render_template('blog.html',all_blog=allblog)


if __name__=='__main__':
    app.run(debug=True)

    
# name='regish'
# gender_response=requests.get(f'https://genderize.io?name=Regish')
# age_response=requests.get(f'https://agify.io?name={name}')

# print(gender_response.json())
# print(age_response.text)

# gender_response_text=gender_response.json()
# gender=gender_response_text['gender']
# print(gender_response_text)
# print("========================")
# print(gender_response_text['json'])
# soup=BeautifulSoup(gender_response_text,'html.parser')
# print(soup)

# print(gender_response_text.find(class_="string"))