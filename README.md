# Smart Factory Analytics

## Overview
The **Smart Factory Analytics** project is a full-stack web application designed to help monitor and manage car manufacturing processes. The project leverages Vue.js with Vite for the frontend and Python with Flask for the backend. It also integrates a PostgreSQL database to manage and store real-time factory data.

## Project Structure
```
Smart-Factory-Analytics/
│
├── devfest_backend/        # Backend (Python Flask)
│   ├── __pycache__/        # Python cache files
│   ├── controllers/        # Backend controllers for handling logic
│   ├── instance/           # Configurations and instance-specific data
│   ├── migrations/         # Database migration files (if using Flask-Migrate/SQLAlchemy)
│   ├── models/             # Database models for entities
│   ├── routes/             # Routes for handling API endpoints
│   ├── app.py              # Main Flask app entry point
│
├── drif_project/           # Frontend (Vue.js with Vite)
│   ├── public/             # Public assets (favicon, index.html, etc.)
│   ├── src/                # Vue.js application source files
│   ├── index.html          # Root HTML file
│   ├── jsconfig.json       # JavaScript configuration
│   ├── package.json        # Frontend dependencies and scripts
│   ├── vite.config.js      # Vite configuration
│
└── README.md               # Project documentation (this file)
```

## Frameworks Used

### Frontend: Vue.js with Vite
- **Vue.js**: A progressive JavaScript framework for building user interfaces. Vue is used to create a responsive and interactive UI.
- **Vite**: A fast build tool and development server for modern web projects. It is used here to bundle and serve the Vue.js frontend quickly and efficiently.

### Backend: Python with Flask
- **Flask**: A lightweight WSGI web application framework in Python. Flask is used to build the backend API and handle HTTP requests.
- **SQLAlchemy (optional)**: An ORM for managing interactions between Flask and PostgreSQL databases.
- **Flask-Migrate (optional)**: A tool for handling database migrations.

### Database

## Authentication & Authorization
The authentication and authorization functionality is handled via a custom page designed using Vue.js, while the backend uses Flask for validating users, JWT tokens, and handling secure API requests.

## Setup Instructions

### 1. Frontend Setup (Vue.js with Vite)

#### Install Dependencies
Before running the frontend, you need to install all the required dependencies.

```bash
cd drif_project
npm install
```

#### Run the Development Server
To run the Vue.js application in development mode, use:

```bash
npm run dev
```

This will start the development server.

### 2. Backend Setup (Python with Flask)

#### Install Python Dependencies
Make sure you have Python installed, then install the necessary backend dependencies. If you are using a virtual environment, activate it first:

```bash
# Activate virtual environment (if applicable)
# source venv/bin/activate (Linux/Mac)
# venv\Scripts\activate (Windows)

# Install Python dependencies
pip install
```

#### Run the Flask Application
To start the Flask backend server, run:

```bash
flask run
```

This will start the Flask development server.

### 3. Running the Full Application

#### Start Backend and Frontend Together
To run both the frontend and backend at the same time, open two terminals:

- **Backend**: Run `flask run` in the `devfest_backend` folder.
- **Frontend**: Run `npm run dev` in the `drif_project` folder.

### 4. Environment Variables
To manage environment-specific settings, such as the database URL, you can use a `.env` file for both backend and frontend configurations.

## Features
- **Real-time Monitoring**: Monitor factory operations, including machine statuses, production lines, and more.
- **Authentication & Authorization**: Secure login with role-based access control.
- **Task Scheduling**: Schedule maintenance tasks based on machine usage.
- **Data Visualization**: Real-time charts and graphs to track energy usage, production rates, etc.
- **Notifications**: Alerts for machine malfunctions or delays in production.

## Conclusion
This project combines the power of **Vue.js** and **Flask** to create a robust platform for smart factory analytics. With a database for data storage, the platform can handle real-time monitoring, efficient task management, and dynamic visualizations if we fully finished it.
