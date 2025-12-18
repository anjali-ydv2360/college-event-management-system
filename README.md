# College Event Management System

A **Django-based web application** for managing college events, registrations, and user accounts. This project enables students to browse and register for events and allows admins to create, update, and manage events — all within a responsive and user-friendly interface.

---

## 🔍 Project Overview

The College Event Management System is designed to automate and streamline event management processes in a college environment. It replaces manual registration and announcement processes with an online platform where event details are published, and students can register with ease.

---

## 📌 Features

- Secure user authentication using Django’s built-in system  
- Students can view upcoming events and register  
- Admin interface for creating, editing, and deleting events  
- Validation to prevent duplicate registrations  
- Organized project with reusable templates and static files

---

## 🛠️ Technologies Used

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** PstgreSQL  
- **Version Control:** Git & GitHub

---

## 📁 Project Structure

```plaintext
college_event_mgmt/
├── accounts/
├── assets/
├── college_event_mgmt/
├── events/
├── media/
├── static/
├── templates/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
└── .gitignore
```
---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/anjali-ydv2360/college-event-management-system.git
cd college-event-management-system
```

### 2. Create a virtual environment
```bash
python -m venv virtual
```
### 3. Activate the virtual environment

Windows
```bash
virtual\Scripts\activate
```

macOS / Linux
```bash
source virtual/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply database migrations
```bash
python manage.py migrate
```

### 6. Run the development server
```bash
python manage.py runserver
```

Open your browser and visit:
http://127.0.0.1:8000/

### Create Admin User (Optional)

To access the Django admin panel:
```bash
python manage.py createsuperuser
```

Admin panel URL:
http://127.0.0.1:8000/admin/

## 🤝 Contribution

Feel free to contribute! Fork the repo → make changes → create a pull request.

GitHub contribution email fix
