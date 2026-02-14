# 📚 Har Ghar Tuition App

> **Bringing Quality Education to Every Home**

A comprehensive web-based tuition management platform built with Django that connects students, parents, and tutors for seamless home tutoring experiences.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-3.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🌟 Features

### For Students & Parents
- 🔍 **Find Tutors**: Search and filter tutors by subject, location, and availability
- 📝 **Book Sessions**: Schedule tuition sessions at your convenience
- 💳 **Secure Payments**: Multiple payment options for hassle-free transactions
- ⭐ **Rate & Review**: Provide feedback on tutors to help others make informed decisions
- 📊 **Progress Tracking**: Monitor student performance and attendance

### For Tutors
- 👤 **Profile Management**: Create detailed profiles showcasing expertise and qualifications
- 📅 **Schedule Management**: Manage availability and booking slots
- 💼 **Resume Upload**: Upload and manage professional credentials
- 💰 **Earnings Dashboard**: Track income and payment history
- 📧 **Communication**: Direct messaging with students and parents

### Admin Features
- 🎯 **Dashboard**: Comprehensive overview of platform activities
- 👥 **User Management**: Manage students, tutors, and parents
- 📈 **Analytics**: Track platform metrics and performance
- ✅ **Verification**: Verify tutor credentials and qualifications
- 🔐 **Security**: Role-based access control and data protection

---

## 🛠️ Tech Stack

- **Backend**: Django 3.0+
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (Development), PostgreSQL (Production)
- **Containerization**: Docker & Docker Compose
- **Static Files**: Django Static Files Management

---

## 📁 Project Structure

```
Har-Ghar-Tuition-App/
├── app/                    # Main application module
├── tution/                 # Core tuition management app
├── static/                 # Static files (CSS, JS, images)
│   └── app/
├── staticfiles/            # Collected static files for production
├── resumes/                # Uploaded tutor resumes
├── db.sqlite3              # SQLite database (development)
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Docker (optional, for containerized deployment)

### Installation

#### Option 1: Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/jjBrij/Har-Ghar-Tuition-App-.git
   cd Har-Ghar-Tuition-App-
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
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and navigate to `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

#### Option 2: Docker Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/jjBrij/Har-Ghar-Tuition-App-.git
   cd Har-Ghar-Tuition-App-
   ```

2. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Open your browser and navigate to `http://localhost:8000`

---

## 🎨 Usage

### For Students/Parents

1. **Register**: Create an account as a student or parent
2. **Browse Tutors**: Search for tutors based on subject, location, and ratings
3. **View Profiles**: Check tutor qualifications, experience, and reviews
4. **Book Session**: Schedule a tuition session at your preferred time
5. **Make Payment**: Complete secure payment for the session
6. **Attend Class**: Join the tuition at scheduled time
7. **Provide Feedback**: Rate and review the tutor after the session

### For Tutors

1. **Register**: Sign up as a tutor
2. **Complete Profile**: Add qualifications, subjects, and upload resume
3. **Set Availability**: Define your available time slots
4. **Receive Bookings**: Get notified when students book your sessions
5. **Conduct Classes**: Teach students at scheduled times
6. **Track Earnings**: Monitor your income through the dashboard

### For Administrators

1. **Login**: Access admin panel at `/admin`
2. **Verify Tutors**: Review and approve tutor applications
3. **Monitor Platform**: Track user activities and platform metrics
4. **Manage Content**: Handle user reports and platform content
5. **Generate Reports**: Create analytics and performance reports

---

## 📸 Screenshots

_Add screenshots of your application here_

```
[Home Page]  [Tutor Listing]  [Profile Page]  [Dashboard]
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (for production)
DB_NAME=tuition_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True

# Payment Gateway (if applicable)
PAYMENT_API_KEY=your-payment-api-key
PAYMENT_SECRET_KEY=your-payment-secret-key
```

---

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Run with coverage:

```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📦 Dependencies

Key dependencies (see `requirements.txt` for complete list):

- Django >= 3.0
- Pillow (for image handling)
- django-crispy-forms (for enhanced forms)
- django-allauth (for authentication)
- gunicorn (for production deployment)

---

## 🚢 Deployment

### Deploying to Production

1. **Set up environment variables** for production
2. **Update `ALLOWED_HOSTS`** in settings
3. **Configure database** (PostgreSQL recommended)
4. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```
5. **Run migrations**
   ```bash
   python manage.py migrate
   ```
6. **Use a production server** (Gunicorn, uWSGI)
   ```bash
   gunicorn tution.wsgi:application --bind 0.0.0.0:8000
   ```

### Docker Deployment

```bash
docker-compose -f docker-compose.prod.yml up -d
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guidelines for Python code
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 🐛 Known Issues

- File upload size limitation for resumes (max 5MB)
- Session scheduling conflicts need manual resolution
- Mobile responsiveness needs improvement on certain pages

---

## 📝 Roadmap

- [ ] Mobile application (iOS & Android)
- [ ] Video conferencing integration
- [ ] AI-powered tutor recommendations
- [ ] Automated attendance tracking
- [ ] Multi-language support
- [ ] Advanced analytics and reporting
- [ ] Payment gateway integration (Stripe, PayPal)
- [ ] SMS notifications
- [ ] Parent-teacher communication portal
- [ ] Assignment submission and grading system

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **jjBrij** - *Initial work* - [GitHub Profile](https://github.com/jjBrij)

---

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap for UI components
- Font Awesome for icons
- All contributors and testers

---

## 📞 Support

For support, questions, or feedback:

- Create an issue in the [GitHub repository](https://github.com/jjBrij/Har-Ghar-Tuition-App-/issues)
- Email: [brijmohan2204@gmail.com]


---

## 📊 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/jjBrij/Har-Ghar-Tuition-App-?style=social)
![GitHub forks](https://img.shields.io/github/forks/jjBrij/Har-Ghar-Tuition-App-?style=social)
![GitHub issues](https://img.shields.io/github/issues/jjBrij/Har-Ghar-Tuition-App-)
![GitHub pull requests](https://img.shields.io/github/issues-pr/jjBrij/Har-Ghar-Tuition-App-)

---

<div align="center">
  <p>Made with ❤️ for quality education</p>
  <p>© 2024 Har Ghar Tuition. All rights reserved.</p>
</div>
