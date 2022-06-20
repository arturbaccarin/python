from imp import reload
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def raiz():
    return {'msg': 'FastAPI na Geek University'}




if __name__ == '__main__':
    import uvicorn

    # uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
    # para qualquer pessoa na rede ter acesso
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)