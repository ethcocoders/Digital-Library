# Modern Digital Library System

This is a full-stack web application designed for the "ወጣት ማእከል ላይብረሪ" (Youth Center Library). It provides students with seamless online access to a digital collection of resources in a modern, intuitive, and aesthetically pleasing interface.

## Features

*   **Authentication:** User registration and login.
*   **Three-Panel Dashboard:** Recent activity, main library content, and user account management.
*   **System Catalogue:** Read-only collection of folders and files managed by administrators.
*   **My Books (Custom Folders):** Private, user-managed space for personal PDF files.
*   **Integrated PDF Viewer:** Seamless in-app PDF viewing.
*   **User Profile:** Manage profile picture and change password.
*   **Theme Toggle:** Light and dark mode.
*   **Admin Panel:** Manage system content and users.

## Technology Stack

*   **Backend:** Python with Flask
*   **Database:** SQLite (with Flask-SQLAlchemy and Flask-Migrate)
*   **Frontend:** React.js (with Vite)
*   **Styling:** Material-UI
*   **Containerization:** Docker

## Setup and Installation

### Prerequisites

*   Docker
*   Node.js and npm (for local frontend development)
*   Python and pip (for local backend development)

### Backend Setup

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Initialize the database and run migrations:
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```
4.  Run the Flask application:
    ```bash
    flask run
    ```

### Frontend Setup

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install Node.js dependencies:
    ```bash
    npm install
    ```
3.  Start the Vite development server:
    ```bash
    npm run dev
    ```

### Docker

1.  Build the Docker image from the project root:
    ```bash
    docker build -t library-app .
    ```
2.  Run the Docker container:
    ```bash
    docker run -p 5000:5000 library-app
    ```
    The application will be accessible at `http://localhost:5000`.

## Usage

1.  **Register/Login:** Access the application and create a new account or log in with existing credentials.
2.  **Browse Content:** Navigate through system files or manage your personal "My Books" collection.
3.  **Upload Files:** Upload your PDF documents to your custom folders.
4.  **Read:** Open any PDF file directly within the integrated viewer.
5.  **Manage Account:** Update your profile picture, change your password, or toggle between light and dark themes.
6.  **Admin Features:** (For administrators only) Manage system-wide content and user accounts.

## Contributing

Contributions are welcome! Please feel free to fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License.

## Powered By

**Ethco Coders**
