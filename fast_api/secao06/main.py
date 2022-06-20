from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app: FastAPI = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)



"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE2NTYyNjQxNTIsImlhdCI6MTY1NTY1OTM1Miwic3ViIjoiMiJ9.MdriWDl_m8XK2AOlHocVYCujwBHrGBJTg1vsvHCAobY
Tipo: bearer
"""