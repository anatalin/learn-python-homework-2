"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem
from collections import Counter


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

def get_user_id_with_most_messages(messages):
    sent_by_user_ids = []
    for m in messages:
            sent_by_user_id = m['sent_by']
            sent_by_user_ids.append(sent_by_user_id)

    
    sent_counter = Counter(sent_by_user_ids)
    most_sent_user_id, _ = sent_counter.most_common(1)[0]

    return most_sent_user_id

def get_most_replied_user(messages):
    messages_by_id = {m['id']: m for m in messages}
    replied_for_users = []
    for m in messages:
        reply_for_id = m['reply_for']
        if reply_for_id is None:
            continue
        reply_for_message = messages_by_id[reply_for_id]
        replied_for_users.append(reply_for_message['sent_by'])
    replies_counter = Counter(replied_for_users)
    most_replied_user_id, _ = replies_counter.most_common(1)[0]

    return most_replied_user_id

def users_most_seen_by_unique_users(messages, take_users):
    user_seen_by_users = {}
    for m in messages:
        if m['seen_by'] is None:
            continue
        user_id = m['sent_by']
        if user_seen_by_users.get(user_id) is None:
            user_seen_by_users[user_id] = set(m['seen_by'])
        else:
            for u_id in m['seen_by']:
                user_seen_by_users[user_id].add(u_id)
    seen_counters = {k: len(user_seen_by_users[k]) for k in user_seen_by_users}
    seen_by_counter = Counter(seen_counters)
    users_ordered = seen_by_counter.most_common(take_users)

    return [most_seen_user for most_seen_user, _ in users_ordered]

def get_most_frequent_messages_daytime(messages):
    morning_count = 0
    day_count = 0
    night_count = 0
    for m in messages:
        hour = m['sent_at'].hour
        if 0 <= hour < 12:
            morning_count += 1
        elif 12 <= hour <= 18:
            day_count += 1
        else:
            night_count += 1
    max_count = max([morning_count, day_count, night_count])
    daytime = ''
    if max_count == morning_count:
        daytime = 'утром'
    elif max_count == day_count:
        daytime = 'днём'
    else:
        daytime = 'вечером'

    return daytime

def get_messages_with_longest_threads(messages, take_count):
    thread_start_ids = [m['id'] for m in messages if m['reply_for'] is None]
    message_and_reply_to = {m['id']: m['reply_for'] for m in messages}
    start_messages_depth = {}
    for id in message_and_reply_to:
        current_id = id
        current_depth = 0
        while current_id not in thread_start_ids:
            current_id = message_and_reply_to[current_id]
            current_depth += 1
        message_depth = start_messages_depth.get(current_id, 0)
        if current_depth > message_depth:
            start_messages_depth[current_id] = current_depth

    messages_depth_counter = Counter(start_messages_depth)
    messages_with_longest_threads = messages_depth_counter.most_common(take_count)

    return [message_id for message_id, _ in messages_with_longest_threads]

if __name__ == "__main__":
    messages = generate_chat_history()
    print(generate_chat_history())
    
    # 1. Вывести айди пользователя, который написал больше всех сообщений.
    result_user_id = get_user_id_with_most_messages(messages)
    print(f'Больше всего написал пользователь {result_user_id}')

    # 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
    result_user_id = get_most_replied_user(messages)
    print(f'Больше всего отвечали на сообщения пользователя {result_user_id}')

    # 3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
    take_users = 5
    most_seen_users = users_most_seen_by_unique_users(messages, take_users)
    print(f'{take_users} пользователей, сообщения которых видело больше всего уникальных пользователей: {most_seen_users}')

    # 4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
    daytime = get_most_frequent_messages_daytime(messages)
    print(f'В чате больше всего сообщений {daytime}')

    # 5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).
    take_messages = 5
    messages_with_longest_threads = get_messages_with_longest_threads(messages, take_messages)
    print(f'{take_messages} сообщений, который стали началом для самых длинных тредов: {messages_with_longest_threads}')