FROM python:3.11-alpine

#Definir o Python como UNBUFFERED
ENV PYTHONUNBUFFERED=1

#Criando o diretório de trabalho
WORKDIR /app

#Copiar arquivo de requirements.txt
COPY requirements.txt ./

#Instalando as bibliotacas necessárias para aplicação
RUN pip install --no-cache-dir -r requirements.txt

#Expor a porta em que a aplicação Gunicorn irá rodar
EXPOSE 9009

#Comando executado ao iniciar o container
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=9009"]

#Cria imagem do projeto e adiciona tag
# docker build --tag api-fornecedor-image .

#Cria container da imagem, **sem redis** mapeia porta 9009 do host p 9009 container, executa em 2° plano o container(detach)
# docker run -p 9009:9009 --name api-fornecedor-container -v .:/app -d api-fornecedor-image

#Criar rede redis
# docker network create redis-network

#Subir o redis
# docker run --network redis-network -d --name redis-container -p 6379:6379 redis:7.2.4-alpine
# docker run -p 9009:9009 --network redis-network --name api-fornecedor-container -v .:/app -d api-fornecedor-image