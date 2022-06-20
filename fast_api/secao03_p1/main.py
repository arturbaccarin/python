from calendar import c
from typing import Optional, Any

from fastapi import FastAPI, HTTPException, status
# from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header

from time import sleep
from fastapi import Depends

from models import Curso
from models import cursos

def fake_db():
    try:
        print('Abrindo a conexão com o banco de dados...')
        sleep(1)
    finally:
        print('Fechando a conexão com o banco de dados...')
        sleep(1)


app = FastAPI(
    title='API de Cursos da Geek University',
    version='0.0.1',
    description='Uma API para estudo do Fast API',
    )


# normalmente dois gets -> um para trazer todos e um para trazer específico
@app.get('/cursos',
        description='Retorna todos os cursos ou uma lista vazia.',
        summary='Retorna todos os cursos',
        response_model=list[Curso],
        response_description='Cursos encontrados com sucesso.')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


# http://localhost:8000/cursos/b -> se for outra coisa que não inteiro ele já dá msg erro como resposta
# gt - greater than
# lt - less than
@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(default=None, title='ID do curso', description='Deve ser entre 1 e 2', gt=0, lt=3), db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        # curso.update({'id': curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Curso não encontrado')


@app.post('/cursos', status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso

    # if curso.id not in cursos:
    #     cursos[curso.id] = curso
    #     return curso
    # else:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Já existe um curso com ID {curso.id}.')


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Não existe um curso com id {curso_id}')


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        # cursos.pop(curso_id)
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT) -> usar quando corrigir bug
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                    detail=f'Não existe um curso com id {curso_id}')

# get pede dados e não recebe (post)
# query string
@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), x_geek: str = Header(default=None), c: Optional[int] = None):
    soma: int = a + b

    if c:
        soma = a + b + c

    print(f'X-GEEK: {x_geek}') # usado no header
    
    return {"resultado": soma}


if '__main__' == __name__:
    import uvicorn

    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True, debug=True)