import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    blog_request=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    allblog=blog_request.json()
    return render_template("index.html",all_blog=allblog)

@app.route('/post/<id>')
def post(id):
    blog_request=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    allblog=blog_request.json()

    for blog in allblog:
        print(blog['id'])
        if int(blog['id'])==int(id):
            theBlog=blog 
    return render_template('post.html',blog=theBlog)

if __name__ == "__main__":
    app.run(debug=True)
