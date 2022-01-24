# from email import contentmanager
# from lib2to3.pytree import Base  # automatic generated code by fastapi
# from typing import Optional  # automatic generated code by fastapi
from urllib import response
from fastapi import FastAPI, Response, status ,HTTPException
from pydantic import BaseModel

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


class Post(BaseModel):
    title: str
    content: str
    # id: int
    # content: list
    # publish: bool = True
    # rating: Optional[int] = None


# Custom posts
my_posts = [{'title': 'post_1', 'content': 'content of post 1', 'id': 1},
            {'title': 'post_2', 'content': 'content of part 2', 'id': 2}]

app = FastAPI()


# Path operation to get all the posts
# Get all posts
@app.get('/posts')
def get_post():
    return {"data": my_posts}

# Path operation to create and save the post in my_posts variable.
@app.post("/posts")
def create_posts(post: Post):
    # we want to add id by ourself and post object doestn't support item assignment.
    new_post = post.dict()
    new_post['id'] = len(my_posts) + 1
    my_posts.append(new_post)
    return {"Status": "Successfully added post",
            "data": new_post}


# path operation to get a specific post with a specific id.
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message":f"Post with id: {id} not found."}
    return post

# path operation for updating a post 
@app.put("/posts/{id}")
def update_post(id: int, post: Post, response: Response):
    post_to_update = find_post(id)
    if not post_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail={"message": f"Post with id: {id} not found"})
    post_to_update['title'] = post.title
    post_to_update['content'] = post.content
    update_post = find_post(id)
    return {"message": "Successfully Updated Post with id: {id}",
            "data": update_post}

# path operation for deleting a post
@app.delete("/post/{id}")
def delete_post(id: int):
    delete_post(id)


# Adding path parameter in path operation "{id}" to get a specific post.
# @app.get("posts/{id}")
# def get_post():


'''
# Blow is optional filed if user doesn't provide publish filed it set True by default.
# Blow is another Optinal filed if user dones't provide an int value we are going to set None by default.

    
class User(BaseModel):
    f_name: str
    l_name: str
    # publish: bool = True


@app.post("/createposts")
def login(data: User):
    print(data)
    full_name = f"{data.f_name} {data.l_name}"
    return {"message": f"Hello Mr.{full_name.title()}, Welcome to our API"}
'''
