# APK Downloader

This Django project allows users to download APK files and admins to upload them.

**Features:**

- Users can browse and download available APKs.
- Admins can upload new APKs (optional, uncomment `admin.py`).
- Downloads are tracked and displayed.

**Installation:**

1. Create a virtual environment: `python -m venv env`
2. Activate the environment: `source env/bin/activate` (Windows: `env\Scripts\activate`)
3. Install dependencies: `pip install -r requirements.txt`
4. Copy this project directory into your environment.
5. Configure database settings in `apk_downloader/settings.py`.
6. Run migrations: `python manage.py makemigrations` and `python manage.py migrate`
7. Start the development server: `python manage.py runserver`

**Usage:**

1. Visit `http://127.0.0.1:8000/` in your browser.
2. Users can see a list of available APKs and download them.
3. Admins (optional): Login using the admin panel (details in `settings.py`).

**Note:**

- Security must be implemented for production use (e.g., user authentication, validation, escaping).

**Optional:**

- For styling, consider using a CSS framework like Bootstrap.

**Disclaimer:**

This code is for educational purposes only and should not be used in production without proper security measures.
