[<img src="https://img.shields.io/badge/python-3.10%20%7C%203.11-blue">](https://www.python.org/downloads/)
[<img src="https://img.shields.io/badge/Telegram-@me-blue">](https://t.me/OxFF00FF)
[<img src="https://img.shields.io/badge/Group-Hamster_Mayhem-blue">](https://t.me/+SUekzTWJlq8yNzIy)


![1](https://github.com/user-attachments/assets/bc847b2b-721c-42f4-b78d-dd6872c5b865)

> 🇪🇳 README in english available [here](https://github.com/OxFF00FF/Hamster_Mayhem/blob/master/README_en.md)

 
Проект был создал чтобы помочь людям проходить рекламные игры в [Hamster Kombat](https://t.me/hamsTer_kombat_bot/start?startapp=kentId1476571560).
По вопросам проекта можете писать в телеграм или в [группу](https://t.me/+SUekzTWJlq8yNzIy)

🔔  Для желающих поддержать проект, доступны способы оплаты:  🔔

- 💎  USDT TON (TON): `UQCjwbMX96YhA4POYlbE3v0M7Xx9TlvjX7bqnJIj0KFVfYlR`

- 💎  USDT TRC20 (Tron): `TK7v5F2HFEErUCFVmy4z53bwdwvZWNNzkz`

- 💎  Toncoin (TON): `UQCjwbMX96YhA4POYlbE3v0M7Xx9TlvjX7bqnJIj0KFVfYlR`

- 💎  Bitcoin (BTC): `188BPS54Pkjaa8uZ8CDdZegBwWP1iwxdrG`

- 💎  Notcoin (NOT): `UQCjwbMX96YhA4POYlbE3v0M7Xx9TlvjX7bqnJIj0KFVfYlR`

- 💎  [Boosty](https://boosty.to/oxff00ff)

- 💎  [Donationalerts](https://www.donationalerts.com/r/oxff00ff)

- 💎 [Paypal]()


## Обновление
 -  (10.09) Теперь можно улучшить карту из списка выгодных карт, нужно в главном меню написать номер карты (например $1, $2 и тд)

 -  (09.09) Добавил доке образ https://hub.docker.com/r/oxff00ff/hamster_mayhem_service

 -  (03.09) Добавлен перевод интерфейса на английский язык. Чтобы поменять язык нужно в настройках выбрать пункт 4 и перезайти

 -  (01.09) В главном меню теперь есть настройки (s)
   
 - Чтобы вам было не так скучно ждать генерацию промокодов,
   была добавлена возможность изменять индикатор загрузки 😉

   Команда `spinner_<num>` выбирает индикатор (например `spinner_1`).

   Команда `list`, показывает все доступные варианты имён и номер, который нужно указать в `spinner_<num>`.

   Команда `default`, установит индикатор по умолчанию


 - Мы сделали телеграм бота для генерации ключей:

   🌐  https://t.me/Hamster_Mayhem_bot

   В будущем планируется сделать активацию промокодов и использование всех доступных активностей в хомяке из бота.
   Сейчас доступна только генерация промокодов и информация о комбо и шифре.

## Возможности
- Переключение между несколькими аккаунтами
- Добавлены все игры
- Можно запускать с вашего Android смартфона
- Генерация промокодов для всех доступных игр
- Генераация сразу для всех игр одновременно (рекомендуется 1-2 за раз)
- Отправка сгенерированных промокодов в вашу группу или в любой чат через бота
- Возможность автоматически применять промокоды в аккаунте после генерации
- Список самых выгодных карт для покупки который обновляется по мере улучшения карт (в списке будут только те что вы можете купить)
- Прохождение миниигры со свечами
- Выполннение комбо и покупка отдельных карт
- Прохождение ежедневного шифра
- Завершение заданий (просмотр видео и ежедневные задания)
- Выполнение кликов и использование буста
- Отображнние оставшегося время для всех активностей

Чтобы использовать несколько аккаунтов нужно в `.env` файле указать несколько токенов.
В таком формате `HAMSTER_TOKEN_x`. Напрмиер `HAMSTER_TOKEN_1`, `HAMSTER_TOKEN_2` и тд.
По умолчанию используется `HAMSTER_TOKEN_1` если других не указано.
Чтобы переключиться на другой аккаунт, нужно выбрать пункт `a` в меню и номер аккаунта.

## ⚙ [Настройки](https://github.com/OxFF00FF/Hamsters_mayhem/blob/master/.env.example)
| Настройка                    | Описание                                                                                      |
|------------------------------|-----------------------------------------------------------------------------------------------|
| **HAMSTER_TOKEN**            | Ваш `Bearer` токен из браузерной версии игры                                                  |
| **TELEGRAM_BOT_TOKEN**       | Токен вашего телеграм бота (необязательно). Нужен для того чтобы отправлять промокоды в вашу группу или в любой другой чат|
| **CHAT_ID**                 | ID вашей группы, канала или пользователя (необязательно). Можно узнать добавив бота `(t.me/GetMy1D_bot)` или аналог в чат. Чтобы бот мог отправлять сообщения нужно добавить его в группу или канал, если в личных сообщениях то нужно отправить команду `/start`     |
| **GROUP_URL**                | Url вашей группы (необязательно). Находится в `Управление группой -> пригласительные ссылки`. Если указано то в консоли буедет уведомление в какую группу он отправил сообщение|

## Предварительные условия
Убедитесь, что у вас установлен Python версии 3.10 или 3.11 (при установке обязательно поставьте галочку в `add python to PATH`):
- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [Python 3.11](https://www.python.org/downloads/release/python-3110/)


## Быстрый старт windows
1. Скачайте zip архив и распакуйте в удобное место
2. Если у вас установлен `git`, откройте удобную для вас папку, нажмите `CTRL + L`, напишите `cmd` и нажмите `enter`
    у вас откроется консоль, встввьте команду и нажмите enter. В эту папку скачается проект.
>`git clone https://github.com/OxFF00FF/Hamster_Mayhem.git`

3. Чтобы установить зависимости, запустите файл `INSTALL.bat`.
4. Для запуска используйте файл `1. START.bat`. Если установлен **Windows Terminal** то `2. START_WT.bat`
5. Настройте `.env` файл. Укажите свой `HAMSTER_TOKEN` и другие значения, если необходимо.
6. Для обновления используйте файл `UPDATE.bat` (если установлен [git](https://git-scm.com/downloads) )

В обычном cmd терминале windows у вас скорее всего не будут работать цвета в консоли и эмоджи.
Для красивого отображения установите 
[windows terminal](https://apps.microsoft.com/detail/9n0dx20hk701?hl=en-US&gl=US) или из папки `Windows Terminal setup`

## Быстрый старт Docker
1. Скачайте и установите [Docker](https://www.docker.com/get-started/)
2. в консоли вводим команду `docker run -d --name hamster_mayhem_USERNAME -e HAMSTER_TOKEN_1="XXX" -e TELEGRAM_BOT_TOKEN=XXX -e CHAT_ID=XXX oxff00ff/hamster_mayhem_service`
и замените XXX на выши данные

· HAMSTER_TOKEN_1 - Ваш hamster token bearer

· TELEGRAM_BOT_TOKEN - Токен телеграм бота, который будет отправлять сообщения

· CHAT_ID - ID группы куда бот будет отправлять сообщения

· USERNAME - Ваш никнейм или другой текст для того чтобы понимать для кого запущен бот (необязательно)

## Как получить hamster Bearer token

>1. Зайдите в свой аккаунт через браузер по номеру или по коду.

![1](https://github.com/user-attachments/assets/0f307b70-b5fa-4479-9ffa-fe0cad537a9e)

>2. Зайдите в бота [hamster kombat bot](https://t.me/hamsTer_kombat_bot/start?startapp=kentId1476571560).
    Нажмите старт и кнопку `играть в 1 клик` или `play`.
    У вас попросят разрешение открыть сайт, соглашаемся нажав на `confirm`

![2](https://github.com/user-attachments/assets/b95141ed-c44e-4853-ad2e-de47e463c18e)
![3](https://github.com/user-attachments/assets/5975d491-2b28-4b70-bf8f-1558ab3c8683)

>4. У вас откроется игра с предложением открыть ее на телефоне.
    но нам это не нужно. Открываем инструменты разработчика.
    Для Chrome нажимаем `F12` или `CTRL + SHIFT + I`
    либо нажмите на `три точки -> дополнительные инструменты -> инструменты разработчика`

![4](https://github.com/user-attachments/assets/610bf810-6d66-4a35-ad08-a558275bf939)

>5. В инструментах разработчика открываем вкладку `Elements`
    и нажимаем на кнопку справа со стрелочкой, наводим на qr код и нажимаем лкм

![123123123](https://github.com/user-attachments/assets/b01121d8-11f5-42a5-9ffd-2596bc855d2e)

>6. У вас откроются элементы и справа нужно найти элемент `iframe` 

![5](https://github.com/user-attachments/assets/b99f849a-568d-42c0-8de8-edf28adb4fa1)

>7. Нажмите 2 раза лкм, и ссылка станет доступной для редактирования.
    Примерно в середине нужно найти `tgWebAppPlatform=weba`

![6](https://github.com/user-attachments/assets/7536093e-b1cf-4183-93e3-e31cba21e73b)

>8. Нужно изменить `tgWebAppPlatform=weba` на `tgWebAppPlatform=android` и нажать emter. 
    У вас откроется игра в браузере

![7](https://github.com/user-attachments/assets/c463489e-bd83-4ea9-8daa-6a81e960514e)

>9. Длаее нажимаем на вкладку `Network` и в нем `All` и нажимаем на значек с перечерунутым кругом

![8](https://github.com/user-attachments/assets/320d8eb3-f3c2-4589-ad47-1445a6a4b50c)

>10. У вас все очистится. и нужно сделать 1 тап в хомяке.

![9](https://github.com/user-attachments/assets/3592748b-5629-4e64-83e4-7cf88ef5d5b1)

>11. Через пару секунд у вас появится запрос. Нажимаем на него. 
    Появятся дополнительные сведения о запросе.
    Нужно нажать на `Headers` и внизу найти `Request headers` (смотрите чтобы **Request Method** запроса был **POST**)

![11](https://github.com/user-attachments/assets/aceb418e-87c5-4746-b515-29cfa0bff660)

>13. Прокручиваем вниз и тут слева есть `Authorization` а справа нужное нам значение. 
     Это и есть токен. Нужно скопировать его полностью от Bearer до последней цифры

![12](https://github.com/user-attachments/assets/a68c821c-ebe1-4829-8897-29ca5908fdff)

>14. Этот токен нужно будет поставить в `.env` файле в `HAMSTER_TOKEN` между кавычек, в **одну строку без переносов**.
>
Например:
>`HAMSTER_TOKEN_1="Bearer 2367343478565fuiGOLjkhegyWEkjeruGFjEkjueowhefiwehggergerUTquvnmpoifehkFwugnjle6732593756"`




# Как запустить код на android

1. Скачать [Termux](https://trashbox.ru/files30/1963775/termux-app_v0.118.1github-debug_universal.apk/) и ввести команды
2. `pkg update && pkg install git` Соглашаемся с установкой (y)
3. `pkg install python` Соглашаемся с установкой (y)
4. `git clone https://github.com/OxFF00FF/Hamster_Mayhem.git`
5. `cd Hamster_mayhem`
6. `cp .env.example .env`
7. `nano .env`. Укажите ваш токен в HAMSTER_TOKEN и другие значения, если необходимо
8. Нажать кнопку `CTRL` и на клавиатуре английскую `X` потом `Y` и `enter` чтобы сохранить файл
9. Проверить что данные записались `cat .env` (выводит содержимое файла .env)
10. Установка зависимостей `pip install -r requirements.txt` 
11. Если будут ошибки во время установки то `pip install python-dotenv requests beautifulsoup4 fuzzywuzzy fake-useragent spinners`
12. Либо по отдельности:
- `pip install python-dotenv`
- `pip install requests`
- `pip install beautifulsoup4`
- `pip install fuzzywuzzy`
- `pip install fake-useragent`
- `pip install spinners`
13. Запускаем `python main.py`
14. Чтобы обновить код используйте команды `git pull` и `python main.py`
15. Если при открытии Termux у вас будет открыта корневая папка `~ $`.
Вам нужно будет перейти в папку проекта `cd Hamsters_mayhem` и запустить `python main.py`

### Видео инструкция
https://github.com/user-attachments/assets/cadbd13e-e932-4e30-9cec-e7a231d4a748


