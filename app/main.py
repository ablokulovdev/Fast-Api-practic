from fastapi import FastAPI


app = FastAPI()

posts = [
    {
        "id": 1,
        "title": "FastAPI bilan REST API yaratish",
        "description": "FastAPI yordamida sodda CRUD API yaratish va validatsiya qo‘shish.",
        "content": "Ushbu maqolada FastAPI framework yordamida RESTful API yaratamiz. "
                   "Pydantic modellari orqali request validatsiyasi, dependency injection, "
                   "va async endpointlar bilan ishlash ko‘rib chiqiladi."
    },
    {
        "id": 2,
        "title": "Django ORM Performance Tuning",
        "description": "Django ORM query optimizatsiyasi va indekslash strategiyalari.",
        "content": "Bu maqolada select_related, prefetch_related, indekslar yaratish "
                   "va N+1 query muammosini bartaraf etish usullari tushuntiriladi. "
                   "Production muhitida query profiling qilish ham ko‘rib chiqiladi."
    },
    {
        "id": 3,
        "title": "PostgreSQL Normalizatsiya Qoidalari",
        "description": "1NF, 2NF va 3NF normal formalari va amaliy misollar.",
        "content": "Ma’lumotlar bazasini normalizatsiya qilish — redundant ma’lumotlarni "
                   "kamaytirish va ma’lumotlar yaxlitligini ta’minlash uchun zarur. "
                   "Har bir normal forma real jadval misolida tushuntiriladi."
    },
    {
        "id": 4,
        "title": "Async Programming Python’da",
        "description": "Async/await, event loop va concurrency tushunchalari.",
        "content": "Async dasturlash I/O bound operatsiyalarni tezlashtirish uchun ishlatiladi. "
                   "asyncio event loop ishlash mexanizmi va concurrent task bajarish "
                   "misollari bilan ko‘rib chiqiladi."
    },
    {
        "id": 5,
        "title": "JWT Authentication Mexanizmi",
        "description": "JWT token asosida authentication va authorization.",
        "content": "JWT (JSON Web Token) stateless authentication mexanizmi hisoblanadi. "
                   "Access token va refresh token arxitekturasi, tokenni tekshirish "
                   "va xavfsizlik best practice’lari bayon qilinadi."
    },
    {
        "id": 6,
        "title": "Clean Architecture Backend’da",
        "description": "Layered architecture va dependency inversion prinsipi.",
        "content": "Clean Architecture maintainable va testable backend tizim qurish "
                   "uchun ishlatiladi. Domain, Application va Infrastructure layerlar "
                   "ajratilishi va dependency injection ishlatilishi tushuntiriladi."
    }
]



@app.get("/posts")
def get_posts():
    return posts


@app.get("/posts/{post_id}")
def get_one_post(post_id : int | None=None):
    for post in posts:
        
        if post["id"] == post_id:
            return post
        
        else:
            return {
                "Message": "Mavjud task yuq"
            }


@app.post("/posts")
def add_posts(post:dict):
    posts.append(post)
    
    return post

@app.put("/posts/{post_id}")
def update_post(post_id:int, new_post: dict):
    for post in posts:
        if post['id'] == post_id:
            post.update(new_post)
            
            return post


@app.delete("/posts/{post_id}")
def delete_post(post_id:int | None = None):
    for post in posts:
        if post["id"]==post_id:
            posts.remove(post)
            
            return post