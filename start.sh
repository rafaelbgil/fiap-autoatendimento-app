#!/bin/sh
#Arquivo de start via docker
echo "Executando espera de 5 segundos para assegurar que o mysql ja esta no ar"
sleep 5
python manage.py makemigrations api
python manage.py migrate 
python manage.py loaddata django-inicial-data.yaml
echo "########################################################################"
echo "|FIAP POS-TECH (Autoatendimento lanchonete)                            |"
echo "|------------------------------------------------                      |"
echo "|Instrucoes de uso:                                                    |"
echo "|Swagger: http://127.0.0.1:8000/api/swagger                            |"
echo "|Redoc: http://127.0.0.1:8000/api/redoc                                |"
echo "|                                                                      |"
echo "|Link doc DDD(toda a doc no miro):                                     |"
echo "| https://miro.com/app/board/uXjVMnTeAN8=/?share_link_id=984815149799  |"
echo "########################################################################"

python manage.py runserver 0.0.0.0:8000
