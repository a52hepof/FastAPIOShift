from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'data': 'Hello  FastAPI!'}

@app.get('/message')
def index():
    return {
    	'año': '2022',
    	'curso': '3º',
    	'asignatura':'gsad',
    	'alumno':'a52hepof'

    }

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)
