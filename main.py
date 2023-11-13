from fastapi import FastAPI

from photo.photo_api import photo_router

app = FastAPI(docs_url='/')

app.include_router(photo_router)

@app.get('/test')
async def test():
    return 'This is test page'
