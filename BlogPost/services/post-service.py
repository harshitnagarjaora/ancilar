
import time, uuid
from stores.posts_store import posts
from stores.comments_store import comments

def _make_id():
    return str(uuid.uuid4())

def create_post(data):
    title = data.get("title")
    content = data.get("content")
    if not title or not content:
        raise ValueError("title and content required")

    post_id = _make_id()
    post = {
        "id": post_id,
        "title": title,
        "content": content,
        "createdAt": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    posts[post_id] = post
    return post

def get_all_posts():
    return list(posts.values())

def update_post(post_id, data):
    if post_id not in posts:
        raise KeyError
    post = posts[post_id]
    if "title" in data:
        post["title"] = data["title"]
    if "content" in data:
        post["content"] = data["content"]
    return post

def delete_post(post_id):
    if post_id not in posts:
        raise KeyError
    # cascade delete comments
    to_delete = [cid for cid, c in comments.items() if c["postId"] == post_id]
    for cid in to_delete:
        del comments[cid]
    del posts[post_id]
