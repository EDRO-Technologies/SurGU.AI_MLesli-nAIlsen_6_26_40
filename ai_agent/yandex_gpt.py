from yandex_cloud_ml_sdk import YCloudML
from dotenv import load_dotenv
import os


root_path = os.path.dirname(__file__)
env_path = os.path.join(root_path, '..', '.env')

load_dotenv(dotenv_path=env_path)

FOLDER_ID = os.getenv("AI_FOLDER_ID")
TOKEN = os.getenv("AI_TOKEN")

sdk = YCloudML(
    folder_id=FOLDER_ID,
    auth=TOKEN,
)
model = sdk.models.completions("yandexgpt")


def preprocess_text(text: str):
    return text.replace("```", "")


def get_answer_ai(lesson_name: str, desc: str, material: str, user_question: str, temp=0.5):
    global model
    model = model.configure(temperature=temp)
    ai_answer = model.run(f"Ты - AI-репетитор. \n"
                          f"Название урока: {lesson_name}\n"
                          f"Описание урока: {desc}\n"
                          f"Контекст урока: '{material}\n'."
                          f"Вопрос студента: '{user_question}'.\n"
                          "Дай развернутый, но четкий ответ, основанный на предоставленных данных. Если ответа в данных нет, так и скажи.")
    return preprocess_text(ai_answer.alternatives[0].text)


def generate_task(lesson_name: str, desc: str, temp=0.5):
    global model
    model = model.configure(temperature=temp)
    ai_answer = model.run(f"Ты - AI-репетитор. Сгенерируй одну практическую задачу по теме: "
                          f" '{lesson_name}, описание темы: {desc}'. Задача должна быть уникальной и проверять понимание ключевых концепций. "
                          f"Уровень сложности - начальный. Предоставь также эталонное решение для проверки. Ответ пришли СТРОГО В JSON формате с ключом 'task' и 'answer'. В ответе должен быть чиствый JSON без форматирования текста и специальных символов.")
    return preprocess_text(ai_answer.alternatives[0].text)


def compare_answers(user_answer, true_answer, temp=0.5):
    global model
    model = model.configure(temperature=temp)
    ai_answer = model.run(
        f"Ты - AI-репетитор. Сравни ответ студента '{user_answer}' с эталонным решением '{true_answer}'. Является ли ответ студента верным? Ответь ТОЛЬКО 'true' или 'false'.")
    return preprocess_text(ai_answer.alternatives[0].text)

def generate_comp_profile(statistic: str, temp=0.5):
    global model
    model = model.configure(temperature=temp)
    ai_answer = model.run(
        f"Ты - AI-репетитор. \n"
        f"Формат: Название области компетенции: уровень знаний, после каждой компетенции переносить на новую строку. Разметка в виде html и тег только <b> ЗАКРЫВАЙ ВСЕ ТЕГИ КОРРЕКТНО. В начале не указывай ``` и тип текста. Добавляй смайлики строго по контексту.\n"
        f"Условие: сгенерируй в красивом формате под response в телеграмм боте. В начале должна быть надпись 'Результат анализа Ваших тестов:' жирным шрифтом, потом уровень компетенций и ниже комментарии и направления для развития.\n"
        f"По нижеприведенным данным о результатах выполнения тестов по разным темам сгенерируй профиль компетенций: \n"+ statistic)
    return preprocess_text(ai_answer.alternatives[0].text)

def generate_theme_blocks(text: str, temp=0.5):
    global model
    model = model.configure(temperature=temp)
    ai_answer = model.run(
        f"Ты - AI-репетитор. \n"
        f"Формат: JSON, где каждая тема - ключ, а текст к нему - значение."
        f"По нижеприведенному тексту сгенерируй четкий формат данных, разделяя каждую тему и добавляя к ней текст строго по документу. Текст:\n" + text)
    return ai_answer.alternatives[0].text