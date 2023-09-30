from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import random

app = FastAPI(
    title="Homchik"
)

app.mount("/static", StaticFiles(directory="static"), name = "static")


templates = Jinja2Templates(directory="templates")

rand_num = ""

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request,  "rand_num": rand_num})

@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def read_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

"""
@app.get("/")
async def get_random_number(request: Request):
    rand_num = random.randint(0, 100)
    return templates.TemplateResponse("home.html", {"request": request, "rand_num": rand_num})
"""
@app.get("/button")
async def get_random_number():
    global rand_num
    rand_num = random.randint(0, 100)  # Генерируем случайное число от 1 до 100
    return RedirectResponse(url="/", status_code=303)

