# Create a Post.
def create_post(post, my_posts):
    post['id'] = len(my_posts) + 1
    my_posts.append(post)
    return post

# Read/Find/Get a perticular Post.
def find_post(id, my_posts):
    for item in my_posts:
        if item['id'] == id:
            return item     # not item = False,  found
    return False            # not False = True,  404 not found

# Update post
def update_post(id, updating_post, post):
    updating_post['title'] = post.title
    updating_post['content'] = post.content
    
# Remove a perticular post.
def remove_post(id, my_posts):
    item = find_post(id)
    if item:
        my_posts.remove(item)
    return False