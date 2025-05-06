from flask import Flask, render_template
from post import Post
import requests

def get_post():
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    post_objects = []
    for post in posts:
        post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
        post_objects.append(post_obj)
    return post_objects

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    post_objects = get_post()
    for post in post_objects:
        print(post.id,"///" ,post.title,"///" ,post.subtitle)    
    return render_template("index.html", blog_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    post_objects = get_post()
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    print(requested_post.id,"///" ,requested_post.title,"///" ,requested_post.subtitle)    
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)