USERS = [
    {"username": "testowy1", "email": "user1@gmail.com", "password": "12345678"},
    {"username": "testowy2", "email": "user2@gmail.com", "password": "12345678"},
    {"username": "testowy3", "email": "user3@gmail.com", "password": "12345678"},
]

CATEGORIES = [
    {"name": "kategoria_1", "description": "to jest kategoria 1"},
    {"name": "kategoria_2", "description": "to jest kategoria 2"},
    {"name": "kategoria_3", "description": "to jest kategoria 3"},
]

POSTS = [
    {
        "id": "7b53a375-7a80-4c40-80ed-929f4115308d",
        "title": "tytuł posta nr 1",
        "content": "to jest zawrtosc posta nr 1",
        "author": "testowy1",
    },
    {
        "id": "2bc8b02a-d290-4340-afb8-f82837597098",
        "title": "tytuł posta nr 2",
        "content": "to jest zawrtosc posta nr 2",
        "author": "testowy1",
    },
    {
        "id": "53a2c9f7-cb7d-45d0-9a93-973f586f4ceb",
        "title": "tytuł posta nr 3",
        "content": "to jest zawrtosc posta nr 3",
        "author": "testowy2",
    },
    {
        "id": "c5c5c283-cfeb-4790-91a5-2e6ce3da704b",
        "title": "tytuł posta nr 4",
        "content": "to jest zawrtosc posta nr 4",
        "author": "testowy2",
    },
    {
        "id": "f468f4e4-886c-43d6-98f4-41285820dce2",
        "title": "tytuł posta nr 5",
        "content": "to jest zawrtosc posta nr 5",
        "author": "testowy3",
    },
    {
        "id": "e8ae3835-db7a-4e37-ab47-6e906941bb43",
        "title": "tytuł posta nr 6",
        "content": "to jest zawrtosc posta nr 6",
        "author": "testowy1",
    },
]

POST_CATEGORIES = [
    {"post_id": "7b53a375-7a80-4c40-80ed-929f4115308d", "categories": ["kategoria_1"]},
    {"post_id": "2bc8b02a-d290-4340-afb8-f82837597098", "categories": ["kategoria_2"]},
    {"post_id": "53a2c9f7-cb7d-45d0-9a93-973f586f4ceb", "categories": ["kategoria_3"]},
    {
        "post_id": "c5c5c283-cfeb-4790-91a5-2e6ce3da704b",
        "categories": ["kategoria_1", "kategoria_2"],
    },
    {
        "post_id": "f468f4e4-886c-43d6-98f4-41285820dce2",
        "categories": ["kategoria_2", "kategoria_3"],
    },
    {
        "post_id": "e8ae3835-db7a-4e37-ab47-6e906941bb43",
        "categories": ["kategoria_2", "kategoria_3"],
    },
]

COMMENTS = [
    {
        "post_id": "7b53a375-7a80-4c40-80ed-929f4115308d",
        "content": "pierwszy komentarz",
        "author": "testowy1",
    },
    {
        "post_id": "7b53a375-7a80-4c40-80ed-929f4115308d",
        "content": "drugi komentarz",
        "author": "testowy2",
    },
    {
        "post_id": "7b53a375-7a80-4c40-80ed-929f4115308d",
        "content": "pierwszy komentarz",
        "author": "",
    },
]
