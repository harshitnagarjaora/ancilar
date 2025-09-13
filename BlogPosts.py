import flask 
from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask
import RESTAPI 
from flask import request, jsonify
app = flask.Flask(__name__)
A = [] # in-memory storage for simplicity

@app.route('/post', methods=['POST'])
def create_post():
    data = request.get.json()
    new_post = BlogPost(id=data['id'],title=data['title'], content=data['content'], created_at=data['created_at'])
    A.append(new_post)
    return jsonify({'message': 'Post created successfully'}), 201

@app.route('/posts', methods=['GET'])
def retrivee_posts():
    posts= [{'id': post.id,'postid' : post.Id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in A]
    return jsonify(posts), 200

@app.route('posts/:id', methods=['PUT'])
def update_posts():
    data = request.get.json()
    for post in A:
        if post.id == data['id']:
            post.title = data['title']
            post.content = data['content']
            return jsonify({'message': 'Post updated successfully'}), 200
    return jsonify({'message': 'Post not found'}), 404

@app.route('posts/:id', methods=['DELETE'])
#Remove a post and all its comments.
#Post: { id: string, title: string, content: string, createdAt: Date }
#Comment: { id: string, postId: string, author: string, text: string, createdAt: Date }
def delete_posts_comment():
    data = request.get.json()
    for post in A:
        if post.id == data['id']:
            A.remove(post)
            return jsonify({"message": "Post deleted successfully"}), 200
    return jsonify({"message": "Post not found"}), 404

@app.route('/posts/:id/comments', methods=['POST'])
def add_comment_to_post():
    data = request.get.json()
    for post in A:
        if post.id == data['postId']:
            new_comment = Comment(id=data['id'], postId=data['postId'], author=data['author'], text=data['text'], created_at=data['created_at'])
            post.comments.append(new_comment)
            return jsonify({'message': 'Comment added successfully'}), 201
    return jsonify({'message': 'Post not found'}), 404

@app.route('/posts/:id/comments', methods=['GET'])
def get_comments_for_post():
    post_id = request.view_args['id']
    for post in A:
        if post.id == post_id:
            comments = [{'id': comment.id, 'postId': comment.postId, 'author': comment.author, 'text': comment.text, 'created_at': comment.created_at} for comment in post.comments]
            return jsonify(comments), 200
    return jsonify({'message': 'Post not found'}), 404

@app.route('/comments/:id', methods=['DELETE'])
def delete_comment()
    comment_id = request.view_args['id']
    for post in A:
        for comment in post.comments:
            if comment.id == comment_id:
                post.comments.remove(comment)
                return jsonify({'message': 'Comment deleted sucessfully'}), 200
    return jsonify({'message': 'Comment not found'}), 404








