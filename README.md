# 📝 DJANGO BLOG PROJECT

Backend infrastructure built with **Django 5.2**, featuring a robust content management system, automated image handling, and cloud storage integration.

---

## 🛠 Tech Stack
* **Framework:** Python 3.x / Django 5.2
* **Database:** SQLite (Dev) / PostgreSQL ready (`psycopg2`)
* **Storage:** AWS S3 (Media & Static files via `boto3` & `django-storages`)
* **Static Assets:** WhiteNoise for efficient static file serving.
* **Environment:** `django-environ` for secure configuration.

---

## 🚀 Architecture Highlights
* **S3 Persistence:** Fully integrated with AWS S3 to handle media uploads, ensuring data persistence on ephemeral filesystems.
* **Relational Schema:** Optimized Database schema with Many-to-Many relationships for Tags and One-to-Many for Authors/Comments.
* **Production Ready:** Configured with `SecurityMiddleware` and `WhiteNoise` for seamless deployment.
* **Logic-Driven:** Custom "Read Later" functionality and slug-based URL routing for SEO-friendly paths.

---

## 🔗 Core Endpoints (Showcase)

| Method | Endpoint | Description | Access |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | Starting Page (Latest Posts) | Public |
| **GET** | `/posts` | Complete Post Archive & Search | Public |
| **GET** | `/posts/<slug>` | Detailed Post View & Comments | Public |
| **POST** | `/posts/<slug>` | Submit New Comment | Public |
| **GET/POST** | `/read-later` | Stored User Reading List | Public |
| **GET** | `/admin/` | Content Management Dashboard | Admin |

---

## ⚙️ Local Setup

```bash
# 1. Clone the repository
git clone <your-repo-url>

# 2. Enter directory
cd <your-project-folder>

# 3. Setup environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start Server
python manage.py runserver

👤 AuthorKyriakos Ververidis Backend Python DeveloperGreece - Open to RemoteEmail | LinkedIn📝 LicenseThis project is open-source and free to use for educational purposes. License: MIT License.