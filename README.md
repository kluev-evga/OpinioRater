# OpinioRater

[![python version](https://img.shields.io/static/v1?label=Python&message=3.11.2&color=97ca00&style=for-the-badge)](https://python.org)
[![django version](https://img.shields.io/static/v1?label=DJANGO&message=3.2.0&color=77ca00&style=for-the-badge)](https://www.djangoproject.com/)
[![drf version](https://img.shields.io/static/v1?label=DRF&message=3.12.4&color=97ca00&style=for-the-badge)](https://www.django-rest-framework.org/)
![api version](https://img.shields.io/static/v1?label=API%20VERSION&message=1.0.0&color=77ca00&style=for-the-badge)
[![licence](https://img.shields.io/static/v1?label=LICENSE&message=MIT&color=97ca00&style=for-the-badge)](https://github.com/kluev-evga/api_final_yatube/blob/master/LICENSE)

## О ПРОЕКТЕ

Проект - это RESTful API, разработанный для сбора отзывов пользователей о различных произведениях, таких как книги,
фильмы и музыка. Этот API предоставляет удобный и эффективный способ для пользователей выражать свое мнение и оценивать
произведения в различных категориях развлечений.

Основные функции API включают:

1. Регистрация и аутентификация пользователей: Пользователи могут создавать учетные записи и аутентифицироваться для
   доступа к сервису.

2. Добавление отзывов: Пользователи могут оставлять отзывы и комментарии к книгам, фильмам и музыке, выражая свои мнения
   и рецензии.

3. Рейтинг и оценка: Пользователи могут проставлять оценки и рейтинги произведениям, что позволяет другим пользователям
   легче находить популярные и рекомендуемые работы.

4. Поиск и фильтрация: API предоставляет возможность поиска произведений по различным критериям, таким как жанр, автор,
   режиссер и многое другое.

5. Интеграция с произведениями: С помощью API можно получать информацию о книгах, фильмах и музыке из внешних
   источников, обогащая базу данных произведений.

6. Аналитика и отчеты: Администраторы могут получать отчеты о активности пользователей и популярности произведений.

Этот проект предоставляет платформу для обмена мнениями и рекомендациями, помогая пользователям находить интересные
произведения и делиться своими впечатлениями.

Stack проекта: Django, Django-rest-framework, simpleJWT, sqlite

### Команда разработки:

<a href='https://github.com/Siktorovich' title='Артём'>
<img src="https://avatars.githubusercontent.com/u/107465356?v=4" width="100" alt="developer Артём">
</a>
<a href="https://github.com/lesinn1k" title='Никита'>
<img src="https://avatars.githubusercontent.com/u/118612161?v=4" width="100" alt="developer Никита">
</a>
<a href='https://github.com/kluev-evga' title='Евгений'>
<img src="https://avatars.githubusercontent.com/u/97233323?v=4" width="100" alt="developer Евгений">
</a>

## ЗАПУСК ПРОЕКТА

<hr/>
<details close>
<summary><h4 style="display: inline">WINDOWS <h3 style="display: inline">▶️</h3></h4></summary>

_Клонировать проект_

```shell
git clone https://github.com/kluev-evga/api_yamdb.git
```

_Установить локальное окружение_

```shell
python -m venv venv
```

_Активировать окружение_

```shell
venv\Scripts\activate           # PowerShell
```

```shell
source venv/Scripts/activate    # Git Bash(Bash)
```

_Установить зависимости_

```shell
pip install -r requirements.txt
```

_Перейти в папку с проектом_

```shell
cd .\api_yamdb\
```

_Выполнить миграции_

```shell
python3 manage.py migrate
```

_запустить сервер_

```shell
python3 manage.py runserver
```

</details>
<hr/>

<details open>
<summary><h4 style="display: inline">LINUX & MacOS<h3 style="display: inline">▶️</h3></h4></summary>

_Клонировать проект_

```shell
git clone https://github.com/kluev-evga/api_yamdb.git
```

_Установить локальное окружение_

```shell
python3 -m venv venv
```

_Активировать окружение_

```shell
source venv/bin/activate
```

_Установить зависимости_

```shell
pip install -r requirements.txt
```

_Перейти в папку с проектом_

```shell
cd .\api_yamdb\
```

_Выполнить миграции_

```shell
python3 manage.py migrate
```

_запустить сервер_

```shell
python3 manage.py runserver
```

</details>
<hr/>

## БАЗА ДАННЫХ

База данных построена на основе SQLITE.  
[Схема](https://dbdocs.io/kluev.evga/api_aymdb?view=relationships) базы данных создана при
помощи [DBML](https://www.dbml.org/docs/#project-definition) синтаксиса и приложения [dbdocs](https://dbdocs.io/).  
Файл схеммы [graph-db.dbml](https://github.com/kluev-evga/api_yamdb/blob/master/graph-db.dbml).

[Установка](https://dbdocs.io/docs) и запуск приложения dbdocs:

```shell
npm install -g dbdocs
```

```shell
dbdocs login
```

выбрать метод аутентификации Email, указать свой email, скопировать код из email и вставить в консоль

```shell
dbdocs build graph-db.dbml
```

Последний шаг выведет в консоль ссылку на задеплоенный проект.

## Добавление данных из csv файлов

Команда для добавления данных из csv

_перейти в папку с проектом_

```shell
cd api_yamdb
````

_добавить все файлы из папки api_yamdb/static/data_

```shell
python3 manage.py import_data_csv
```

_добавить отдельный файл:_

```shell
python3 manage.py import_data_csv —[file name].csv
```

## Регистрация и авторизация

```mermaid
graph LR
api/v1/auth/signup-->POST;
POST-->user-exists?;
user-exists?-->yes-->skip-->Email_confirmation_code;
user-exists?-->no-->create-user-->Email_confirmation_code;
```

```json
{
  "email": "user@example.com",
  "username": "john_doe"
}
```🔊

JWT

```mermaid
graph LR
api/v1/auth/token-->POST-->JWT-token;
```

```json
{
  "username": "john_doe",
  "confirmation_code": "blyxv3-48b382b52eb0d5885cd281ca10a85839"
}
```

## ЛИЦЕНЗИЯ

Распространяется по `MIT` лицензии. Для дополнительной информации
смотри: [LICENSE](https://github.com/kluev-evga/api_yamdb/blob/master/LICENSE)
