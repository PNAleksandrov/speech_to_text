хакатон ЭКСМО / тестовые задания

Backend разработка

Описание задачи:

1. На серверной стороне должна быть реализована возможность распознавания 
   голосовых сообщений с помощью API асинхронного распознавания.
2. Приложение должно иметь возможность записывать голосовые сообщения 
   в режиме реального времени и отправлять их на сервер для распознавания.
3. Приложение должно иметь возможность распознавать голосовые сообщения,
   сохраненные в формате аудиофайла, и выводить результат на экран.

Требования к реализации:

1. Для работы приложения необходимо получить API-ключ от сервиса API асинхронного распознавания.
2. Приложение должно предоставлять пользователю возможность записи голосовых сообщений и 
   отправки их на сервер для распознавания.
3. Приложение должно иметь возможность распознавания голосовых сообщений в формате аудиофайла.
4. Приложение должно выводить результат распознавания голосовых сообщений на экран/консоль.
5. Код должен быть выложен на GitHub и содержать инструкцию по запуску приложения.

Данное приложение позволят записывать аудио файл сохранять его на сервер асинхронного 
распознавания речи и выводить распознанный текст в консоль.

Для запуска данное программы необходимо:
1. Скачать данный код, установить и активизировать виртуальное окружение.
2. Далее необходимо установить необходимые библиотеки из файла requirements.txt
3. В фале api_key.py необходимо вписать api-ключ для работы с сервером 
   асинхронного распознавания речи Yandex SpeechKit. Также необходимо вписать ключи
   и имя бакета для доступа к YndexStorage, где будет храниться аудиофайл.
4. Далее необходимо запустить файл main.py В консоли появиться сообщение 
   "Recording... 5 sec" голос будет записывать 5 секунд.
   (данный интервал времени можно установить в параметре RECORD_SECONDS) 
    после чего в консоли появится надпись "Recording finished." и запись остановиться.
   Через некоторое время в консоли появится распознанный текст из голосового сообщения.


