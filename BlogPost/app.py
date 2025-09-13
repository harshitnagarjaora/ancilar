from flask import Flask, request, jsonify
from services import post_service, comment_service

app = Flask(__name__)

# ---------------- Posts ----------------
@app.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    try:
        post = post_service.create_post(data)
        return jsonify(post), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(post_service.get_all_posts())

@app.route("/posts/<post_id>", methods=["PUT"])
def update_post(post_id):
    data = request.json
    try:
        post = post_service.update_post(post_id, data)
        return jsonify(post)
    except KeyError:
        return jsonify({"error": "Post not found"}), 404

@app.route("/posts/<post_id>", methods=["DELETE"])
def delete_post(post_id):
    try:
        post_service.delete_post(post_id)
        return "", 204
    except KeyError:
        return jsonify({"error": "Post not found"}), 404


# ---------------- Comments ----------------
@app.route("/posts/<post_id>/comments", methods=["POST"])
def add_comment(post_id):
    data = request.json
    try:
        comment = comment_service.add_comment(post_id, data)
        return jsonify(comment), 201
    except KeyError:
        return jsonify({"error": "Post not found"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/posts/<post_id>/comments", methods=["GET"])
def list_comments(post_id):
    try:
        comments = comment_service.get_comments_for_post(post_id)
        return jsonify(comments)
    except KeyError:
        return jsonify({"error": "Post not found"}), 404

@app.route("/comments/<comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    try:
        comment_service.delete_comment(comment_id)
        return "", 204
    except KeyError:
        return jsonify({"error": "Comment not found"}), 404


# Health check
@app.route("/", methods=["GET"])
def health():
    return {"ok": True}


if __name__ == "__main__":
    app.run(debug=True)
