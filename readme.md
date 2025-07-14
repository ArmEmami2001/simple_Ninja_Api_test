# 📚 Simple Ninja API Test

A minimal Django project demonstrating a RESTful API for managing books using the [Ninja-Extra](https://ninja-extra.dev/) framework.

## 🚀 Features

- List all books
- Create a new book
- Retrieve a single book by ID
- Admin panel integration
- Basic automated tests with Django's test client

## 🏗️ Project Structure

```
armemami2001-simple_ninja_api_test/
├── Books/                # App for book-related logic
│   ├── controllers.py    # API routes with Ninja-Extra
│   ├── models.py         # Book model
│   ├── schema.py         # Pydantic schemas for API
│   ├── tests.py          # Unit tests for API
│   └── ...
├── Library/              # Main Django project
│   ├── api.py            # Ninja API configuration
│   ├── settings.py       # Django settings
│   └── urls.py           # URL routing
├── manage.py             # Django CLI entrypoint
└── requirements.txt      # Project dependencies
```

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/simple_ninja_api_test.git
cd simple_ninja_api_test
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Start the development server**

```bash
python manage.py runserver
```

## 🧪 Running Tests

```bash
python manage.py test
```

## 📬 API Endpoints

Base path: `/api/`

| Method | Endpoint            | Description            |
|--------|---------------------|------------------------|
| GET    | `/books`            | List all books         |
| POST   | `/books`            | Create a new book      |
| GET    | `/books/{book_id}`  | Retrieve a book by ID  |

### Example POST Payload
```json
{
  "title": "1984",
  "author": "George Orwell"
}
```

## 🛠️ Admin Access

1. Create a superuser:
```bash
python manage.py createsuperuser
```

2. Visit the admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## 📦 Built With

- [Django 5.2.2](https://www.djangoproject.com/)
- [Ninja-Extra](https://ninja-extra.dev/)
- SQLite (default Django database)

## 📝 License

This project is licensed under the MIT License.

---

> Project bootstrapped by [@armemami2001](https://github.com/armemami2001)
