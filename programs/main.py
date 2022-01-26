# from email import contentmanager
# from lib2to3.pytree import Base  # automatic generated code by fastapi
# from typing import Optional  # automatic generated code by fastapi
# from urllib import response
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from crud import create_post, find_post, update_post, remove_post

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


# Get all posts
@app.get('/posts')
def get():
    return {"data": my_posts}

# Create and save post in my_posts variable.
@app.post("/posts")
def create(post: Post):
    # We want to add id by ourself and post object doestn't support item assignment.
    new_post = create_post(post.dict(), my_posts)
    return {"message": "Successfully created a post with id {id}",
            "data": new_post}

# Get one specific Post using path parameter.
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id, my_posts)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"Post with id {id} was not found."}
    return {"message": f"Successfully found post with id {id}.",
            "data": post}

# Update post
@app.put("/posts/{id}")
def update(id: int, post: Post):
    get_post = update_post(id, post, my_posts)      # get post from database
    if not get_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={"message": f"Post with id {id} was not found."})
    # post_to_update['title'] = post.title
    # post_to_update['content'] = post.content
    # updated_post = find_post(id) # after updation get post from database
    # update_post(id, updating_post, post)
    # updated_post = find_post(id, my_posts)
    # if not updated_post:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail={"message": f"Post with id: {id} not found"})
    return {"message": f"Successfully updated post with id {id}.",
            "data": get_post}

# Delete a post
@app.delete("/posts/{id}")
def delete_post(id: int):
    deleted_post = remove_post(id, my_posts)
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail={"message": f"The post with id {id} was not found."})
    
    return {"message": f"Successfully removed post with id {id}.",
            "data": deleted_post}
    
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
