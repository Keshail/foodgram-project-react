# FOODGRAM
Сайт - http://84.201.177.244

[![foodgram-project workflow](https://github.com/Keshail/foodgram-project-react/actions/workflows/mainl.yml/badge.svg)](https://github.com/Keshail/foodgram-project-react/actions/workflows/main.yml)


<p><a href="https://www.python.org/" rel="nofollow"><img src="https://camo.githubusercontent.com/938bc97e6c0351babffcd724243f78c6654833e451efc6ce3f5d66a635727a9c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d507974686f6e2d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d507974686f6e" alt="Python" data-canonical-src="https://img.shields.io/badge/-Python-464646??style=flat-square&amp;logo=Python" style="max-width:100%;"></a>
<a href="https://www.djangoproject.com/" rel="nofollow"><img src="https://camo.githubusercontent.com/99e48bebd1b4c03828d16f8625f34439aa7d298ea573dd4e209ea593a769bd06/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d446a616e676f2d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d446a616e676f" alt="Django" data-canonical-src="https://img.shields.io/badge/-Django-464646??style=flat-square&amp;logo=Django" style="max-width:100%;"></a>
<a href="https://www.docker.com/" rel="nofollow"><img src="https://camo.githubusercontent.com/038c45c7c5f0059723bba28b5b77bd9ac7994c8da774814c8fcb620f4bc61b35/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d646f636b65722d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d646f636b6572" alt="docker" data-canonical-src="https://img.shields.io/badge/-docker-464646??style=flat-square&amp;logo=docker" style="max-width:100%;"></a>
<a href="https://www.postgresql.org/" rel="nofollow"><img src="https://camo.githubusercontent.com/18b5ef277b89701f948c212d45d3460070037bda9712fe5f1e64315811356ea2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d506f737467726553514c2d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d506f737467726553514c" alt="PostgreSQL" data-canonical-src="https://img.shields.io/badge/-PostgreSQL-464646??style=flat-square&amp;logo=PostgreSQL" style="max-width:100%;"></a>
<a href="https://www.sqlite.org/index.html" rel="nofollow"><img src="https://camo.githubusercontent.com/2c46c2b57530e634094dcb5ca341adbd8cc101300fd0968991b2a2700f1ac318/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d53514c6974652d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d53514c697465" alt="SQLite" data-canonical-src="https://img.shields.io/badge/-SQLite-464646??style=flat-square&amp;logo=SQLite" style="max-width:100%;"></a>
<a href="https://github.com/"><img src="https://camo.githubusercontent.com/ca897bbf26e1c6429197c0c0f53e16f1625eaa99d0bc8caa4934c4b12ece45a1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d4769744875622d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d476974487562" alt="GitHub" data-canonical-src="https://img.shields.io/badge/-GitHub-464646??style=flat-square&amp;logo=GitHub" style="max-width:100%;"></a>
<a href="https://github.com/features/actions"><img src="https://camo.githubusercontent.com/b70fe9e64e76d385b8cae9b6366dfba69af953e85d16cf43bb1f9d46fefb1621/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d476974487562253230416374696f6e732d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d476974487562253230616374696f6e73" alt="GitHub%20Actions" data-canonical-src="https://img.shields.io/badge/-GitHub%20Actions-464646??style=flat-square&amp;logo=GitHub%20actions" style="max-width:100%;"></a>
<a href="https://nginx.org/ru/" rel="nofollow"><img src="https://camo.githubusercontent.com/b9f9edede39c7f898e25e81ce431f7c4b8d0b375c05768fd6916e599fcba219f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d4e47494e582d3436343634363f3f7374796c653d666c61742d737175617265266c6f676f3d4e47494e58" alt="NGINX" data-canonical-src="https://img.shields.io/badge/-NGINX-464646??style=flat-square&amp;logo=NGINX" style="max-width:100%;"></a></p>

## Описание
«Продуктовый помощник» Сайт является - базой кулинарных рецептов. Пользователи могут создавать свои рецепты, читать рецепты других пользователей, подписываться на интересных авторов, добавлять лучшие рецепты в избранное, а также создавать список покупок и загружать его в txt формате. Также присутствует файл docker-compose, позволяющий , быстро развернуть контейнер базы данных (PostgreSQL), контейнер проекта django + gunicorn и контейнер nginx

## Для развертывания данного проекта необходимы следующие действия:
- Скачать проект с SSH (на самом деле вам нужна только папка 'infra/')
```
git@github.com:Keshail/foodgram-project-react.git 
```
- Подключиться на свой сервер:
```
ssh <server user>@<server IP>
```
- Установить Docker на свой сервер:
```
sudo apt install docker.io
```
- Установить Docker Compose (for Linux)
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
- Получить разрешения на docker-compose
```
sudo chmod +x /usr/local/bin/docker-compose
```
- Создайте каталог проекта (желательно в вашем домашнем каталоге)
```
mkdir foodgram && cd foodgram/
```
- Создать env-file:
```
touch .env
```
- Заполните env-file как указано ниже:
```
DEBUG=False
SECRET_KEY=<Your_some_long_string>
ALLOWED_HOSTS='localhost, 127.0.0.1, <Your_host>'
CSRF_TRUSTED_ORIGINS='http://localhost, http://127.0.0.1, http://<Your_host>'
DB_ENGINE='django.db.backends.postgresql'
DB_NAME='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD=<Your_password>
DB_HOST='db'
DB_PORT=5432
```
- Скопируйте файлы из 'infra/' (на вашем локальном компьютере) на ваш сервер:
```
scp infra/* <server user>@<server IP>:/home/<server user>/foodgram/
```
- Run docker-compose
```
sudo docker-compose up -d
```
## Приятного пользования :)
При необходимости вы можете использовать предложенный список ингредиентов для написания рецептов. Загрузите его в базу данных с помощью следующей команды
```
sudo docker exec -it foodgram_backend_1 python manage.py loaddata data/dump.json
```
## Backend by:
https://github.com/Keshail
## Frontend by:
https://github.com/yandex-praktikum/foodgram-project-react
