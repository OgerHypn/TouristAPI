# TouristAPI
1.   > ___pip install -r requirements.txt___

2.   > ___запустить docker-compose.yml___


3. Отправить POST запрос по адресу http://127.0.0.1:1234/submitData с JSON в Body в соответствии с примером:
{ "beauty_title": "пер. ", "title": "Черкесия", "other_titles": "Рона", "connect": "test",

"add_time": "2023-09-05 15:18:16", "user": {"email": "qwerty@mail.ru", "fam": "Иванов", "name": "Иван", "otc": "Иванович", "phone": "+7 999 99 99"},

"coords":{ "latitude": "54.4656", "longitude": "9.4577", "height": "1500"}, "level": {"winter": "1A", "summer": "1А", "autumn": "1А", "spring": "2A"},

"images": [{"data":"<картинка1>", "title":"Альпы"}, {"data":"<картинка>", "title":"Вершина"}] }
