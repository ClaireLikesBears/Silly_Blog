from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

# Folder where your .txt blog posts are stored
BLOG_FOLDER = 'blog_posts'  

# Function to get the list of blog posts
def get_blog_posts():
    # Get all .txt files in the blog folder
    files = [f for f in os.listdir(BLOG_FOLDER) if f.endswith('.txt')]
    posts = []
    for file in files:
        file_path = os.path.join(BLOG_FOLDER, file)
        with open(file_path, 'r') as f:
            content = f.read()
        post_title = file.replace('.txt', '')  # Use filename as title
        posts.append({'title': post_title, 'content': content, 'filename': file})
    return posts

@app.route('/')
def home():
    posts = get_blog_posts()
    return render_template('index.html', posts=posts)

@app.route('/post/<filename>')
def post(filename):
    file_path = os.path.join(BLOG_FOLDER, filename)
    with open(file_path, 'r') as f:
        content = f.read()
    return render_template('post.html', content=content, title=filename.replace('.txt', ''))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

