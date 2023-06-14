from sentence_transformers import SentenceTransformer as SBERT
from catboost import CatBoostClassifier
import pyaudio
import wave
import speech_recognition

sbert1 = SBERT('sberbank-ai/sbert_large_nlu_ru')
classifier = CatBoostClassifier().load_model('catboost-sbert', format='cbm')


def get_embedding(command: str):
    return sbert1.encode(command)


def predict_intent_code(command: str):
    return classifier.predict(get_embedding(command))[0]


def record_audio(rec_sec: int):
    """ Records rec_sec-second audio and saves it to "last_command.wav" file """
    CHUNK = 1024
    FRT = pyaudio.paInt16
    CHAN = 1
    RT = 16000
    REC_SEC = rec_sec  # длина записи
    OUTPUT = "last_command.wav"

    p = pyaudio.PyAudio()
    stream = p.open(format=FRT, channels=CHAN, rate=RT, input=True,
                    frames_per_buffer=CHUNK)  # открываем поток для записи

    # здесь показываем, что запись началась
    print("rec, say something!")
    frames = []
    for i in range(int(RT / CHUNK * REC_SEC)):
        data = stream.read(CHUNK)
        frames.append(data)
    # здесь показываем, что запись завершилась
    print("done")

    stream.stop_stream()  # останавливаем запись
    stream.close()  # закрываем поток
    p.terminate()

    w = wave.open(OUTPUT, 'wb')
    w.setnchannels(CHAN)
    w.setsampwidth(p.get_sample_size(FRT))
    w.setframerate(RT)
    w.writeframes(b''.join(frames))
    w.close()


def speech_to_text(rec_sec: int):
    """ Records voice command and returns its transcript"""
    record_audio(rec_sec)
    sample = speech_recognition.WavFile('last_command.wav')
    recognizer = speech_recognition.Recognizer()

    with sample as audio:
        recognizer.adjust_for_ambient_noise(audio)
        content = recognizer.record(audio)
    return recognizer.recognize_wit(content, key="")
