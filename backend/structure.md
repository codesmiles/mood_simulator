your_fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── migrations/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── item_service.py
│   └── api/
│       ├── __init__.py
│       ├── v1/
│       │   ├── __init__.py
│       │   ├── endpoints/
│       │   │   ├── __init__.py
│       │   │   ├── users.py
│       │   │   └── items.py
│       │   └── api.py
│       └── api.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_users.py
│   └── test_items.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md