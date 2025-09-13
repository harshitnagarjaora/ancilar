import time, uuid
from stores.posts_store import posts
from stores.comments_store import comments

def _make_id():
    return str(uuid.uuid4())

def add_comment(post_id, data):
    if post_id not in posts:
        raise KeyError
    author = data.get("author")
    text = data.get("text")
    if not author or not text:
        raise ValueError("author and text required")

    comment_id = _make_id()
    comment = {
        "id": comment_id,
        "postId": post_id,
        "author": author,
        "text": text,
        "createdAt": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    comments[comment_id] = comment
    return comment

def get_comments_for_post(post_id):
    if post_id not in posts:
        raise KeyError
    return [c for c in comments.values() if c["postId"] == post_id]

def delete_comment(comment_id):
    if comment_id not in comments:
        raise KeyError
    del comments[comment_id]
