# ДЗ часть1
  В этой части реализован проект quotes без использования БД.
  Для запуска и проверки функционала первой части:
1. Создать venv: `python3 -m venv <venv_name>`
2. Активировать venv: `source venv_name/bin/activate`
3. Установите зависимости: `pip install -r requirements.txt`
4. Функционал находится в файле app_with_out_db.py
   (Переименуйте файлы app_with_out_db.py в app.py, а app.py в app_with_db.py)
5. Запустите сервер из терминала `flask run --debug 127.0.0.1:5000`

### блок-1
- [x] Реализована функция возвращающая цитату по id, если не найдена функция вернет сообщение с кодом 404
- [x] Реализована функция возвращающая колличество цитат
- [x] Реализована функция возвращающая случайную цитату 



### блок-2
- [x] Реалезована функция добавляющая новую цитату и отдельная функция возвращающая новый уникальный id
- [x] Реализована функция редактирования цитаты
- [x] Реализована функция удаления цитаты
- [x] Добавлен рейтинг цитаты в словарь цитат и реалезована функция получения цитаты по фильтру
- [x] Реализован функционал, позволяющий получить все цитаты с рейтингом в указанном диапазоне.

### Коллекция Postman
- [x] Коллекция Postman находится в файле Flask1.postman_collection.json в корне проекта

# ДЗ часть2
  В этой части проект переделан под использование БД.
  Для запуска и проверки функционала второй части части:
1. Если не создан, создать venv: `python3 -m venv <venv_name>`
2. Активировать venv: `source venv_name/bin/activate`
3. Если не установленны, установите зависимости: `pip install -r requirements.txt`
4. Функционал находится в файле app.py
   Если файл был переименован для проверки первой части переименуйте обратно в app.py 
5. Создайте репозиторий миграции `flask db init`
6. Cоздать первоначальную миграцию `flask db migrate -m "Initial migration"`
7. Применить изменения к БД `flask db upgrade`
8. Cоздать записи в БД например с помощью POSTMAN:
   `127.0.0.1:5000/authors` - создать автора
   `127.0.0.1:5000/authors/1/quotes` - создать цитату для автора.
    Или через терминал:
   `from app import db, QuoteModel, AuthorModel` затем создать автора `author = AuthorModel("Цой")`,
   `db.session.add(author)` , `db.session.commit()` затем добавить автору цитату `q1 = QuoteModel(author, 'белый снег,серый лед')
   "белый снег,серый лед")` , `db.session.add(q1)` , `db.session.commit()` 
5. Запустите сервер из терминала `flask run --debug 127.0.0.1:5000`

### блок-1
   - [x] Функции добавления, правки, удаления, получения всех цитат, получения цитаты по id,
         переделанны для работы с бд c помощью ORM
   - [x] Добавлены функции получения всех авторов, автора по id, создания автора
   - [x] Реализована функция поиска по рейтингу и\или автору