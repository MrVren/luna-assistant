'''
Voice assistant v0.1

*********************

В этой версии временно используются готовые фразы персонажа из League of Legends

Комментарии чисто для себя, вряд ли это кто-то еще увидит
'''
import speech_recognition as sr
import pyttsx3

import notifications, fuzzy_comparsion, task_manager
from vocabulary import word_list, name


voice_engine = pyttsx3.init()
while True:
    try:
        recognizer = sr.Recognizer()
        #Необходимо указать свой индекс микрофона. Запускаем "test_microphone.py" и находим свой
        with sr.Microphone(device_index=1) as source:
            #Следующая команда отрезает шумы, прослушивая микрофон в течение примерно 1 секунды
            recognizer.adjust_for_ambient_noise(source)
            print('Слушаю...')
            audio = recognizer.listen(source)

        voice_command = recognizer.recognize_google(audio, language='ru-RU').lower()
        print('Вы сказали: ' + voice_command)
        try:
            print('Начинаю перебор')
            if voice_command.startswith(name):
                if name in voice_command:
                    print('Триггер найден')
                    _task = voice_command

                    _task = _task.replace(name, '').strip()
                    for item in word_list["to_be_removed"]:
                        _task = _task.replace(item, '').strip()
                        
                    task_manager.temp = _task # для запросов
                    _task = fuzzy_comparsion.recognize_cmd(_task)
                    task_manager.execute_cmd(_task['task'])
                else: print('Триггер не найден')
        except sr.UnknownValueError:
            print('[log] Повтори пожалуйста')
        except sr.RequestError:
            print('[log] Проверь интернет')
        except sr.WaitTimeoutError:
            print('[log] Таймаут, проверь интернет')
    except sr.UnknownValueError:
            print('[log] Тишина')
    except sr.RequestError:
            print('[log] Проверь интернет')
    except sr.WaitTimeoutError:
            print('[log] Таймаут, проверь интернет')