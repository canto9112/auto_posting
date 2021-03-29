# Бот публикует посты в Вк, Телеграм, Фуйсбук

Скрипт ```main.py``` запускает бота в Вк, Телеграм и Facebook который публикует
пост во всех трех соцсетях.

### Как установить

У вас уже должен быть установлен Python 3. Если его нет, то установите.
Так же нужно установить необходимые пакеты:
```
pip3 install -r requirements.txt
```

### Как пользоваться скриптом

Для работы скрипта нужно создать файл ```.env``` в директории где лежит скрипт.

#### Настройки для Телеграм

1. Нужно создать бота в телеграм. Написать [Отцу ботов](https://telegram.me/BotFather):
    * /start
    * /newbot
    
2. Отец ботов попросит ввести два имени. 

    * Первое — как он будет отображаться в списке контактов, можно написать на русском. 

    * Второе — имя, по которому бота можно будет найти в поиске. 
      Должно быть английском и заканчиваться на bot (например, notification_bot)

3. Вставьте ваш токен бота в файл ```.env```:
    ```
    TELEGRAM_BOT_TOKEN='95132391:wP3db3301vnrob33BZdb33KwP3db3F1I'
    ```

4. Вам необходимо создать «открытый» канал в Телеграм. 
    * Вставить название канала в файл ```.env```:
        ```
        TELEGRAM_CHANAL_NAME='@auto_posting_vk_tg'
        ```
    * Назначить бота администратором канала:
      - Для этого включим бота, нажав кнопку START;
      - Копируем ссылку на нашего бота;
      - Затем заходим в канал и добавляем бота в администраторы.
        (Не забудьте включить галочку «добавить администратора)
        
             
#### Настройки для Вконтакте
   
1. Для постинга на стену нужен ключ доступа пользователя. Чтобы его получить, нужно создать “standalone приложение”
   на странице [Вконтакте для разработчиков](https://vk.com/dev). 

2. Получите ключ доступа пользователя. Вам потребуются следующие права: photos, groups, wall и offline.

3. Вставьте ваш access_token в файл ```.env```:
    ```
    VK_USER_TOKEN='7485d674495fd9c9ad6c980f40085fad861bc85ae1780d8c880bdc98b3ab60546c05880d249ed3f7e2a46'
    ```

4. Получить group_id для вашей группы. Узнать group_id можно [здесь](https://regvk.com/id/).

5.  Вставьте ваш group_id в файл ```.env```:
    ```
    VK_GROUP_ID='203517016'
    ```
6. Создать альбом в группе и вставить id альбома в файл ```.env```:
    ```
    VK_ALBOUM_ID='280071703'
    ```
    
#### Настройки для Facebook

1. Создать группу в Facebook. Вставить id группы в файл ```.env```:
    ```
    FACEBOOK_GROUP_ID=472212560631956
    ```

2. Создать [приложение](https://developers.facebook.com/):
    * Создать приложение -> Дополнительные параметры -> Другое;
    * Получить токен с помощью браузерного интерфейса к [API Facebook](https://developers.facebook.com/tools/explorer/)
    * Выставить все разрешения (должно получиться 46);
    * [Продлить токен](https://developers.facebook.com/tools/debug/accesstoken/) с 2 часов до 2 месяцев;
    * Вставить токен в файл ```.env```:
        ```
        FACEBOOK_TOKEN='EAAHYcXgwbHkBAMxgltQwcktwUrcf6lJwgU9oJHmU7tCJZA4VfR7EVQ4cvfq08Humcu7E5xTh7
        ```

#### Настройки GOOGLE Таблицы
1. Создать Гугл таблицу и вставить id таблицы в файл ```.env```:
    ```
    GOOGLE_SHEET_ID='1pdTOD7XDU2udLZXADKj-V6ElW7WUNLSA4kU_JqvUKhI'
    ```
2. Создать новый проект в [Google console](https://console.cloud.google.com/);
3. Search product and resource -> Drive Activity API -> ENABLE;
4. Search product and resource -> Google Sheets API -> ENABLE;
5. Создать сервисный аккаунт -> Выбрать роль Project -> Editor;
6. Создать ключ: Service account -> KEYS -> ADD KEY -> Create new kew -> json
7. Сохранить полученный файл json в директорию проекта;
8. Вставить название файла в файл ```.env```:
   ```
   GOOGLE_CONFIG_FILE='google_config.json'
   ```
8. Дать доступ в гугл таблице на E-mail сервисного аккаунта;
9. На первом листе заполнить столбцы:

     | A                     | B                     | C            | D              | 
     | --------------------- |:---------------------:|:------------:|:--------------:|
    1| Текст первого поста   | Ссылка на картинку 1  |   пусто      |   пусто        |   
    2| Текст второго поста   | Ссылка на картинку 2  |   пусто      |   пусто        |         
    3| Текст третьего поста  | Ссылка на картинку 3  |   пусто      |   пусто        |    

### Запуск скрипта
Для запуска бота вам необходимо запустить командную строку и перейти в каталог со скриптом:
```
>>> python3 main.py 3 (где 3 - это номер строки где в А1 - текст, в В1 - ссылка на картинку)
```

### Цели проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
