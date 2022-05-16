# dev-test
### [Dev Test Requirements](/dev-requirements.md "dev-requirements.md link")

## Python fastAPI

* Install locally (Instalar localmente)
Requires MongoDB Atlas DATABASE_LINK= in .env file.
E preciso adicionar um .env file com link de banco de dados MongoDB Atlas DATABASE_LINK= 
```
pip install -r requirements.txt


```
* Run manually
```
uvicorn app.main:app --reload
```
* API Docs
```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```
## Nexe.js Client

* Install

```
cd client
npm install

```
* Run manually

```
npm run dev

```

# Run with Docker
Não tive tempo de implementar a automação docker compose
## Python fastAPI
[dev-test Python API](/Dockerfile "Python API Dockerfile")

## Nextjs Front-end
EM DESENVOLVIMENTO
[dev-test Python API](/client/Dockerfile "Front-end Dockerfile")
