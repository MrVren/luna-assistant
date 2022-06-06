#Здесь описываются все команды
import random
from pydub import AudioSegment
from pydub.playback import play
import webbrowser
import wikipedia
import pyautogui
import asyncio
import notifications, vocabulary



temp = None
def say_done():
    _phrase = random.choice(vocabulary.phrases_done)
    sound = AudioSegment.from_wav(_phrase)
    play(sound)

def execute_cmd(_task):
    print(_task)

    if _task == "say_hi":
        res = random.choice(vocabulary.phrases_hello)
        sound = AudioSegment.from_wav(res)
        play(sound)

    elif _task == "exit_app":
        res = random.choice(vocabulary.phrases_exit)
        sound = AudioSegment.from_wav(res)
        play(sound)
        exit()

    elif _task == "trash_incoming":
        res = vocabulary.phrase_to_trash
        sound = AudioSegment.from_wav(res)
        play(sound)

    elif _task == "about_life":
        res = vocabulary.phrase_about_life
        sound = AudioSegment.from_wav(res)
        play(sound)


    elif _task == "wiki_request":
        wikipedia.set_lang('ru')
        req = temp
        for item in vocabulary.word_list["wiki_request_crop"]:
            req = req.replace(item, '').strip()
            print('команда после обрезки',req)
        try:
            pyautogui.alert(wikipedia.summary(req, sentences=2))
            say_done()
        except wikipedia.exceptions.DisambiguationError:
            print('Уточни запрос')
        
    elif _task == "open_browser":
        webbrowser.open(url="opera://startpage")
        say_done()

    elif _task == "open_youtube":
        link = 'https://youtube.com'
        webbrowser.open_new_tab(url=link)
        say_done()

    elif _task == "hide_all":
        pyautogui.hotkey('win','d')
        say_done()

    elif _task == "praise_luna":
        res = random.choice(vocabulary.laughing)
        sound = AudioSegment.from_wav(res)
        play(sound)

    else: notifications.show_notify(vocabulary.name, 'Я не расслышала\nПовтори пожалуйста')