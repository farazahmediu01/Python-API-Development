
# Create a Post.
def create_post(post, database):
    post['id'] = len(database) + 1
    database.append(post)
    return post

# Read/Find/Get a perticular Post.
def find_post(id, database):
    for item in database:
        if item['id'] == id:
            return item     # not item = False,  found
    return None             # not False = True,  404 not found

# Update post
def update_post(id, post, database):
    get_post = find_post(id, database)
    if not get_post:
        return get_post
    get_post['title'] = post.title
    get_post['content'] = post.content
    return get_post

# Remove a perticular post.
def remove_post(id, database):
    item = find_post(id)
    if not item:
        return item
    item = database.pop(id)
    return item