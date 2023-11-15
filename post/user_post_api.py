from fastapi import APIRouter, UploadFile

from post import PublicPostValidator, EditPostValidator

from database.postservice import add_post_db, add_post_photo_db, edit_post_db, delete_post_db

posts_router = APIRouter(prefix='/user_post', tags=['Работа с публикациями'])


# Запрос на публикации поста
@posts_router.post('/public_post')
async def public_post(data: PublicPostValidator):
    pass

# Запрос на изменения текста в публикации
@posts_router.put('/change_post')
async def change_post(data: EditPostValidator):
    pass

# Запрос на удаления публикации
@posts_router.delete('/delete_post')
async def delete_post(post_id: int):
    pass

# Запрос на получения всех публикаций
@posts_router.get('/get_all_posts')
async def get_all_posts():
    pass

# Запрос для добавления фото к посту
@posts_router.post('/add_photo')
async def add_photo():
    pass

# Получить определенный пост
@posts_router.get('/get_exact_post')
async def get_exact_post(post_id: int):
    pass