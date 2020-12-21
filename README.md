##Сайт обучающей платформы

###В проекте иcпользуются модели:
### Accounts
1. Student - наследуется от User
1. Teacher - наследуется от User

### Courses
1. CourseCategory - категория учебных программ (курсов)
1. Course - сам учебный курс
1. CourseModule - модули учебного курса

### Требования к организации системы

Установить зависимости:

```bash
pip install -r reqs.txt
```

Провести миграции:

```bash
python manage.py migrate
```


Создать суперпользователя:

```bash
python manage.py createsuperuser
```

Загрузить тестовые данные:

```bash
python manage.py loaddata users.json
```
```bash
python manage.py loaddata courses.json
```

