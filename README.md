
#### Creación de imagen 

```bash
docker build . -t coffee-data:latest
```

### Correr la app en docker

```bash
docker run -d -p 8503:8501 coffee-data:latest
```

### Install serverless

Usaremos la version 3.38.0

http://github.com/serverless/serverless/tree/v3.38.0

```bash
npm install -g serverless@3.38.0
```