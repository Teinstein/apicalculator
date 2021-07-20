from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')  # Similar to Flask
async def hello_world():
    return {"Hello": "World"}  # JSON response

# FastAPI can make use of both dynamically and statically typed values
# Additionally, the following examples will demonstrate path and query params


# PATH PARAMETERS

# Dynamic example (accepts any type)

@app.get('/variable/{variable_id}')
async def get_variable(variable_id):
    return { "variable id": variable_id }

"""
In the function decorator, the line '/variable/{variable_id}' in its
entirety is called a Path Parameter. This can be considered as the URL path.
A blank '/' is considered to be the base or root path for the API. As such, 
adding something after it creates a new path (URL). The {variable_id} section 
of the line is an extension of it which we pass in. One can assign any value to
it through the function, and it would constitute a new path. These are used to
dynamically create new URL paths. If i passed in 10 to the path parameter, 
'/variable/10' would be a valid path. If i passed in 'Intern', '/variable/Intern'
would now be a valid path as well. The value type we pass into path parameters 
can also be limited using Python's optional typing class.
"""

# Strongly typed example (one datatype only)
# Note, typing is usually applied in function definitions

@app.get('/strong/{variable_id}')
async def strong_variable(variable_id: int):
    return { "variable_id": variable_id }

# FastAPI also has automatic docs which can be accessed at
# {any_url}/docs


# QUERY PARAMETERS

@app.get('/query/')
async def queries(num: int, text: Optional[str]):
    return {
        "number": num,
        "text": text
    }

"""
This is an example of a query parameter. In this case, we have also generated new
URL paths, but unlike with path parameters, we do not have a predefined path. In this
case, the data we receive from the function must be passed into a 'query' attached to
the initial path. Example, for num = 10, text = 'Intern', the path would be

/query?num=10&text=Intern

Notice how the text parameter has been given an Optional type, meaning it does not need
to be entered and is optional. In this case we will still include the parameter in the
query, but set the text = blank.

/query?num=10&text=

Query parameters are very useful for accessing very specific pages by generating a new
URL based on the given data.
"""