from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/')
def hello_world():
    return {'message': 'hello world'}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=80)
