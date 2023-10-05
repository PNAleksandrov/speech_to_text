import requests
import time
from api_key import api, storage_key, storage_secret_key, buck
import pyaudio
import wave
import boto3

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5  # Время записи звука в секундах
FILENAME = "recorded_audio.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

frames = []

print("Recording... 5 sec")

for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording finished.")

stream.stop_stream()
stream.close()

p.terminate()

wf = wave.open(FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# Ключи для доступа в хранилище.
ACCESS_KEY = storage_key
SECRET_KEY = storage_secret_key

# Укажите имя бакета, куда вы хотите загрузить аудиофайл
BUCKET_NAME = buck

# Укажите путь к аудиофайлу, который нужно загрузить
AUDIO_FILE_PATH = "recorded_audio.wav"

# Инициализация клиента для работы с Object Storage
client = boto3.client('s3',
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY,
                      region_name='ru-central1',
                      endpoint_url='https://storage.yandexcloud.net'
                      )


# Загрузка аудиофайла в бакет
with open(AUDIO_FILE_PATH, 'rb') as audio_file:
    client.upload_fileobj(audio_file, BUCKET_NAME, 'recorded_audio.wav')

time.sleep(7)

# Укажите ваш API-ключ и ссылку на аудиофайл в Object Storage.
key = api

file_url = 'https://storage.yandexcloud.net/bucket-apn1/recorded_audio.wav'

POST = 'https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize'

body = {
    "config": {
        "specification": {
            "languageCode": "ru-RU",
            "model": "general",
            "audioEncoding": "LINEAR16_PCM",
            "sampleRateHertz": "16000",
        }
    },
    "audio": {
        "uri": file_url
    }
}

# Аутентификации через Api Yandex.
header = {'Authorization': 'Api-Key {}'.format(key)}

# Отправить запрос на распознавание.
req = requests.post(POST, headers=header, json=body)
data = req.json()
print(data)

id = data.get('id')
step = 30
tt = 0

# Запрашивать на сервере статус операции, пока распознавание не будет завершено.
while True:

    time.sleep(step)
    tt = tt + step

    GET = 'https://operation.api.cloud.yandex.net/operations/{id}'
    req = requests.get(GET.format(id=id), headers=header)
    req = req.json()

    if req['done']:
        break
    print("Not ready " + str(tt))

# Показать полный ответ сервера в формате JSON.
# print("Response:")
# print(json.dumps(req, ensure_ascii=False, indent=2))

# Показать только текст из результатов распознавания.
print("Распознанный текст:")
for chunk in req['response']['chunks']:
    print(chunk['alternatives'][0]['text'])
