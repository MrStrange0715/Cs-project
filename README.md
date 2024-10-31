# Email Viewer Dashboard 📧

**Email Viewer Dashboard** is a simple, powerful interface for viewing and managing your emails with ease. Developed in Python, this project fetches emails from a specified account, organizes them, and displays key details in a dashboard format, making it easier to navigate and manage your inbox.

![Python Version](https://img.shields.io/badge/python-3.x-blue) ![License](https://img.shields.io/badge/license-MIT-green)

## Features

- **Inbox Summary**: Quickly view recent emails with **sender details** and **preview text**.
- **Search & Filter**: Easily find emails by keywords, sender, date, or subject.
- **Email Viewer**: Open emails directly in the dashboard to read full content.
- **Responsive UI**: Intuitive and user-friendly design, built to simplify navigation.
- **Secure Authentication**: Uses secure authentication to fetch emails from your inbox.

### Prerequisites

- Python 3.x
- Email client credentials (e.g., for Gmail, you’ll need an app password and IMAP enabled)
- Required libraries listed in `requirements.txt`

### Clone Repository

```bash
git clone https://github.com/MrStrange0715/email-viewer-dashboard.git
cd email-viewer-dashboard
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

```bash
EMAIL_ADDRESS=your-email@example.com
EMAIL_PASSWORD=your-password-or-app-specific-password
```

## Usage

```bash
python main.py
```

## Technologies Used

- **Python**: Core programming language
- **IMAP/SMTP Protocols**: For secure email fetching
- **Tkinter / CustomTkinter**: For GUI creation (replace if using other frameworks)
- **dotenv**: For secure configuration management

## Future Enhancements

- **Reply & Forward Options**: Enable direct email replies and forwards within the dashboard.
- **Email Categorization**: Auto-categorize emails into folders such as Promotions, Updates, etc.
- **Notifications**: Real-time email notifications.

##Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.
