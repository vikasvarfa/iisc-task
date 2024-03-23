# IISC Task Web Development
# Object Detection Of transportation-related images

# Demo Video
https://github.com/vikasvarfa/iisc-task/assets/101801409/38b9c9ea-a279-424b-9556-a754ecccb383

This is a web application developed using React for the frontend and Python Flask for the backend.

## Prerequisites

Before running the application, make sure you have the following installed:

- Node.js and npm (for React)
- Yarn package manager
- Python 3

## Installation

### Frontend

1. Navigate to the frontend directory:
    ```
    cd iisc-task-frontend
    ```

2. Install dependencies using Yarn:
    ```
    yarn install
    ```

### Backend

1. Navigate to the backend directory:
    ```
    cd transportation-backend
    ```

2. Create a virtual environment (recommended):
    ```
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
    ```
    venv\Scripts\activate
    ```
    - On macOS and Linux:
    ```
    source venv/bin/activate
    ```

4. Install dependencies:
    ```
    pip install Flask flask-cors opencv-python
    ```

## Running the Application

### Frontend

1. Navigate to the frontend directory:
    ```
    cd iisc-task-frontend
    ```

2. Start the development server:
    ```
    yarn dev
    ```

3. Access the frontend in your browser at [http://localhost:5173](http://localhost:5173).

### Backend

1. Navigate to the backend directory:
    ```
    cd transportation-backend
    ```

2. Make sure the virtual environment is activated (if you created one).

3. Set the Flask app environment variable:
    - On Windows:
    ```
    set FLASK_APP=app.py
    ```
    - On macOS and Linux:
    ```
    export FLASK_APP=app.py
    ```

4. Run the Flask server:
    ```
    python app.py
    ```

5. Access the backend API endpoints at [http://localhost:5000](http://localhost:5000).

## Additional Notes

- Make sure both frontend and backend servers are running simultaneously for the full functionality of the application.
