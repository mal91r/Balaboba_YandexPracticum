import requests

query = 'Если б море было водкой'
genre = 3

def get_genres():
    genres_url = 'https://zeapi.yandex.net/lab/api/yalm/intros'
    try:
    	response = requests.get(genres_url).json()
    	genres_list = response['intros']
    except:
        print('Во время выполнения функции get_genres() возникла ошибка!')
        genres_list = []
    return genres_list

def print_genres(genres_list):
    print("Список жанров, в которых можно продолжить фразу:")
    for line in genres_list:
    	number, style, discription = line
    	print(f'{number}-{style}-{discription}')
def generate_text(query, genre):
    text_url = 'https://zeapi.yandex.net/lab/api/yalm/text3'
    data = {
        "query": query,
        "intro": genre
    }
    try:
    	response = requests.post(url=text_url, json=data)
    	dict_response = response.json()
    except:
        print('Во время выполнения функции generate_text() возникла ошибка!')
        dict_response = {}
    return dict_response

def print_text(text_dict):
    print('\n' + 'Ответ на ваш запрос:' + '\n')
    print(text_dict['query'] + text_dict['text'])

genres_list = get_genres()

print_genres(genres_list)

text_dict = generate_text(query, genre)

print_text(text_dict)
