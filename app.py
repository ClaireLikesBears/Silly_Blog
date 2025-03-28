from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

# Folder where your .txt blog posts are stored
BLOG_FOLDER = 'blog_posts'

# Ensure the folder exists to prevent errors
if not os.path.exists(BLOG_FOLDER):
    os.makedirs(BLOG_FOLDER)

# Function to get the list of blog posts
def get_blog_posts():
    files = [f for f in os.listdir(BLOG_FOLDER) if f.endswith('.txt')]
    posts = []
    for file in files:
        file_path = os.path.join(BLOG_FOLDER, file)
        with open(file_path, 'r', encoding='utf-8') as f:
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
    
    # Handle cases where the file does not exist
    if not os.path.exists(file_path):
        return "Post not found", 404

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return render_template('post.html', content=content, title=filename.replace('.txt', ''))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Railway-assigned port
    app.run(host='0.0.0.0', port=port)
