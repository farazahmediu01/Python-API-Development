# Custom posts
from ast import Return
from turtle import pos

my_posts = list()

# [{'title': 'post_1', 'content': 'content of post 1', 'id': 1},
#            {'title': 'post_2', 'content': 'content of part 2', 'id': 2}]

# Find a perticular post.


def find_post(id):
    for item in my_posts:
        if item['id'] == id:
            return item
    return False

# Create Post.


def create_post(post):
    post['id'] = len(my_posts) + 1
    my_posts.append(post)
    return post


# Remove a perticular post.
def remove_post(id):
    item = find_post(id)
    if item:
        my_posts.remove(item)
