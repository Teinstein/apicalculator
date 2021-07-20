from fastapi import FastAPI, HTTPException
from typing import Optional, Union
import math

app = FastAPI()

@app.get('/')
async def home():
    return { "Welcome": "Home page" }


@app.get('/add/')
async def add(n1: Union[int, float], n2: Union[int, float]):
    return { f"{n1} + {n2}": n1 + n2 }
    

@app.get('/sub/')
async def sub(n1: Union[int, float], n2: Union[int, float]):
    if n2 > n1:
        return { f"{n1} - {n2}": f"-{n2-n1}" }
    return { f"{n1} - {n2}": n1 - n2 }


@app.get('/mul/')
async def mul(n1: Union[int, float], n2: Union[int, float]):
    return { f"{n1} x {n2}": n1 * n2 }


@app.get('/div/')
async def div(n1: Union[int, float], n2: Union[int, float]):
    return { f"{n1} / {n2}": n1 / n2 }


@app.get('/mod/')
async def mod(n1: Union[int, float], n2: Union[int, float]):
    return { f"{n1} % {n2}": n1 % n2 }


@app.get('/power/')
async def power(n1: Union[int, float], n2: Union[int, float]):
    return { f"{n1} ^ {n2}": n1 ** n2 }


@app.get('/exp/')
async def exponent(n1: Union[int, float]):
    return { f"e ^ {n1}": math.exp(n1)}

@app.get('/sqrt/')
async def root(n1: Union[int, float]):
    return { f"root({n1})": math.sqrt(n1)}
    

@app.get('/log/')
async def log(n1: Union[int, float], n2: Union[int, float]):
    return { f"log (base{n1}) {n2}": math.log(n2, n1)}


@app.get('/ln/')
async def ln(n1: Union[int, float]):
    return { f"ln {n1}": math.log(n1, math.e)}


@app.get('/sin/')
async def sin_deg(n1: Union[int, float], deg: bool, inv: bool):
    if not inv:
        if deg:
            rads = math.radians(n1)
            return { f"sin {n1} degrees": math.sin(rads) }
        else:
            return {f"sin pi/{n1} radians": math.sin((math.pi/n1)) }
    else:
        if n1 < -1 or n1 > 1:
            return { f"Error": "Must be in the range of -1 to 1 radians" }
        else:
            return { f"sin inv ({n1})": math.asin(n1) }


@app.get('/cos/')
async def cos_deg(n1: Union[int, float], deg: bool, inv: bool):
    if not inv:
        if deg:
            rads = math.radians(n1)
            return { f"cos {n1} degrees": round(math.cos(rads)) }
        else:
            return {f"cos pi/{n1} radians": math.cos(math.pi/n1) }
    else:
        if n1 < -1 or n1 > 1:
            return { f"Error": "Must be in the range of -1 to 1 radians" }
        else:
            return { f"cos inv ({n1})": math.acos(n1) }


@app.get('/tan/')
async def tan_deg(n1: Union[int, float], deg: bool, inv: bool):
    if not inv:
        if deg:
            rads = math.radians(n1)
            return { f"tan {n1} degrees": math.tan(rads) }
        else:
            return {f"tan pi/{n1} radians": math.tan(math.pi/n1) }
    else:
        if n1 < -1 or n1 > 1:
            deg = False
            return { f"Error": "Must be in the range of -1 to 1 radians" }
        else:
            return { f"tan inv ({n1})": math.atan(n1) }


@app.get('/fact/')
async def factorial(n1: int):
    mul = 1
    for i in range(n1):
        mul *= (i + 1)

    return { f"{n1}!": mul }
