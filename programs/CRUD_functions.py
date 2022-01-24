# Custom posts
my_posts = [{'title': 'post_1', 'content': 'content of post 1', 'id': 1},
            {'title': 'post_2', 'content': 'content of part 2', 'id': 2}]

# Find a perticular post
def find_post(id):
    for item in my_posts:
        if item['id'] == id:
            return item
    return False

# Remove a perticular post.
def remove_post(id):
    item = find_post(id)
    if item:
        my_posts.remove(item)

