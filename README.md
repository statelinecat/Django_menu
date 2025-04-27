# Django Tree Menu Application

## Описание проекта

Это Django-приложение для создания и отображения древовидных меню на сайте. Меню хранятся в базе данных, редактируются через стандартную админку Django и отображаются с помощью специального тега шаблона.

## Основные возможности

- Создание многоуровневых меню с неограниченной вложенностью
- Управление меню через административную панель Django
- Поддержка нескольких независимых меню на одном сайте
- Автоматическое определение активного пункта меню по URL
- Оптимизированные запросы к базе данных (1 запрос на меню)

## Установка и настройка

1. Клонируйте репозиторий:
```
git clone https://github.com/statelinecat/Django_menu
cd Django_menu
```

2. Создайте и активируйте виртуальное окружение:
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```
pip install -r requirements.txt
```

4. Примените миграции:
```
python manage.py migrate
```

5. Создайте суперпользователя для доступа к админке:
```
python manage.py createsuperuser
```

6. Запустите сервер разработки:
```
python manage.py runserver
```

## Использование

1. Добавьте 'menu' в INSTALLED_APPS в settings.py:
```python
INSTALLED_APPS = [
    ...
    'menu',
]
```

2. В нужном шаблоне подключите тег меню:
```html
{% load menu_tags %}
{% draw_menu 'main_menu' %}
```

3. В админке (/admin/) создайте:
   - Объекты Menu (например, 'main_menu', 'secondary_menu')
   - Пункты меню (MenuItem) с указанием родительских элементов

## Структура проекта

- `menu/` - основное приложение
  - `models.py` - модели Menu и MenuItem
  - `admin.py` - настройки админки
  - `templatetags/menu_tags.py` - тег для отрисовки меню
  - `templates/menu/` - шаблоны меню

## Требования

- Python 3.8+
- Django 3.2+

## Лицензия

MIT License