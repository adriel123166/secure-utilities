# 🔐 Secure Utilities System

A comprehensive desktop application providing multiple utility tools with secure user authentication and data management.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)

## 📋 Features

- **🔒 Secure Authentication**: SHA-256 hashing with salt for password security
- **🔗 URL Shortener**: Convert long URLs into compact, shareable links
- **🔢 Advanced Calculator**: Professional calculator with modern UI
- **💬 SMS Messaging**: Send SMS to Philippine mobile numbers (Semaphore API integration)
- **📊 Fake Data Generator**: Generate realistic test data for development
- **🎨 Professional UI**: Modern dark-themed interface with smooth animations

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/adriel123166/secure-utilities.git
   cd secure-utilities
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **First-time setup**
   - The database will be created automatically on first run
   - Register a new account
   - Login and access all utilities

## 📦 Dependencies

```
tkinter (included with Python)
sqlite3 (included with Python)
requests>=2.31.0
```

## 🏗️ Project Structure

```
secure-utilities/
├── main.py                      # Application entry point
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore rules
│
└── src/
    ├── auth/                    # Authentication module
    │   ├── login.py            # Login functionality
    │   ├── register.py         # Registration functionality
    │   └── __init__.py
    │
    ├── database/                # Database layer
    │   ├── db_handler.py       # Database operations
    │   └── __init__.py
    │
    ├── utils/                   # Utility functions
    │   ├── util_shortener.py   # URL shortening
    │   ├── sms_messaging.py    # SMS functionality
    │   ├── fake_data_generator.py # Data generation
    │   ├── password.py         # Password hashing
    │   └── __init__.py
    │
    ├── widgets/                 # UI components
    │   ├── calculator.py       # Calculator widget
    │   └── __init__.py
    │
    └── utilities_menu.py        # Main dashboard interface
```

## 🔧 Configuration

### SMS Messaging (Optional)

To enable real SMS sending via Semaphore:

1. Sign up at [Semaphore](https://semaphore.co/)
2. Get your API key from the dashboard
3. Open `src/utils/sms_messaging.py`
4. Update the API key in `get_sms_config()` function:

```python
"semaphore": {
    "api_key": "YOUR_SEMAPHORE_API_KEY_HERE"
}
```

## 🎯 Usage

### URL Shortener
- Enter a long URL
- Click "Shorten URL"
- Copy the shortened link

### Calculator
- Click "Launch Calculator"
- Perform mathematical operations
- Supports: +, -, ×, ÷, decimals

### SMS Messaging
- Enter Philippine phone number (09XXXXXXXXX)
- Type your message
- Select provider (Simulator or Semaphore)
- Click "Send Message"

### Fake Data Generator
- Enter number of records (1-100)
- Click "Generate Data"
- Use generated data for testing

## 🔐 Security Features

- **Password Hashing**: SHA-256 with unique salt per user
- **No Plain Text**: Passwords never stored in plain text
- **Input Validation**: All inputs sanitized and validated
- **SQL Injection Prevention**: Parameterized queries
- **Session Management**: Secure session handling

## ⌨️ Keyboard Shortcuts

- `Alt + S` - Shorten URL
- `Alt + C` - Open Calculator
- `Alt + M` - Send Message
- `Alt + G` - Generate Fake Data
- `Alt + L` - Logout
- `Esc` - Logout

## 🗄️ Database

The application uses SQLite3 with the following schema:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🛠️ Development Tools

- **Check Database**: Run `python check_database.py` to inspect database contents
- **Quick Check**: Run `python quick_check.py` for fast user verification

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [adriel123166](https://github.com/adriel123166)
- Email: your.felixadriel123@gmail.com

