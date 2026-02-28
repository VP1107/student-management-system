# 🎓 Student Management System

A command-line application for managing student records using Python and MySQL with full CRUD functionality.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- ➕ **Add Students** - Register new students with validation
- 👀 **View Students** - Display all students in formatted table
- ✏️ **Update Grades** - Modify student grades by ID
- 🗑️ **Delete Students** - Remove students with confirmation
- 🛡️ **Error Handling** - Comprehensive exception handling
- 🔒 **Security** - Parameterized queries prevent SQL injection
- 📊 **Formatted Output** - Clean, professional table display

## 🖼️ Screenshots

### Main Menu
```
======================================================================
          STUDENT MANAGEMENT SYSTEM
======================================================================
1. ADD STUDENTS
2. VIEW STUDENTS
3. UPDATE GRADES
4. DELETE STUDENTS
5. EXIT
----------------------------------------------------------------------
```

### View Students
```
======================================================================
ID    Name                 Age   Grade   Email                         
----------------------------------------------------------------------
1     John Doe            20    A       john@example.com              
2     Jane Smith          22    B       jane@example.com              
======================================================================
Total Students: 2
```

## 🛠️ Technologies Used

- **Python 3.7+** - Programming language
- **MySQL 8.0+** - Database management
- **mysql-connector-python** - MySQL driver for Python
- **python-dotenv** - Environment variable management
- **colorama** (optional) - Colored terminal output

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.7 or higher installed
- MySQL Server installed and running
- pip (Python package manager)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/VP1107/student-management-system.git
cd student-management-system
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up MySQL Database

Create a database in MySQL:
```sql
CREATE DATABASE student_db;
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=student_db
```

**⚠️ Important:** Never commit your `.env` file to Git! It's already in `.gitignore`.

### 5. Run the Application
```bash
python main.py
```

The application will automatically create the `students` table on first run.

## 📁 Project Structure
```
student-management-system/
├── main.py              # Main application with menu interface
├── database.py          # Database connection and table creation
├── crud.py              # CRUD operations (Create, Read, Update, Delete)
├── .env                 # Environment variables (not in repo)
├── .env.example         # Example environment file
├── .gitignore           # Git ignore rules
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## 🗄️ Database Schema
```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    grade VARCHAR(1),
    email VARCHAR(50) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🎯 Usage Guide

### Adding a Student
1. Select option `1` from the menu
2. Enter student details:
   - Name
   - Age
   - Grade (A, B, C, etc.)
   - Email (must be unique)

### Viewing All Students
1. Select option `2` from the menu
2. All students will be displayed in a formatted table

### Updating a Grade
1. Select option `3` from the menu
2. Enter the Student ID
3. Enter the new grade

### Deleting a Student
1. Select option `4` from the menu
2. Enter the Student ID
3. Confirm deletion by typing `YES`

## 🔐 Security Features

- ✅ Parameterized SQL queries prevent SQL injection
- ✅ Environment variables protect database credentials
- ✅ Email uniqueness constraint prevents duplicates
- ✅ Input validation for all user inputs
- ✅ Comprehensive error handling with try-except blocks

## 🐛 Error Handling

The system handles:

- ❌ Invalid input types (e.g., non-numeric age)
- ❌ Duplicate email addresses
- ❌ Database connection failures
- ❌ Non-existent student IDs
- ❌ SQL syntax errors
- ❌ Missing environment variables

## 🔮 Future Enhancements

- [ ] Search students by name or email
- [ ] Export data to CSV/Excel
- [ ] Import data from CSV
- [ ] GUI version using Tkinter or PyQt
- [ ] Student attendance tracking
- [ ] Grade analytics and reports
- [ ] Multiple user roles (admin, teacher)
- [ ] RESTful API integration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**

- GitHub: [VP1107](https://github.com/VP1107)
- LinkedIn: [Vatsal Pandya](linkedin.com/in/vatsal-pandya-30a946274)
- Portfolio: [My Website](https://vp1107.github.io/My_Resume/)

## 🙏 Acknowledgments

- Thanks to the MySQL and Python communities
- Inspired by real-world student management needs

## 📞 Support

If you have any questions or run into issues, please open an issue on GitHub.

---

⭐ If you found this project helpful, please give it a star!

