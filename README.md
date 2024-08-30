# Reverse Proxy, Nginx Config, Frontend and Backend App

## Description
This project is designed to demonstrate a complete web application setup involving both frontend and backend components, managed using Docker and Nginx for reverse proxy. The project structure is divided into two main folders: `backend` and `frontend`.

- **Backend:** Contains the core server logic implemented in Python, along with a `Dockerfile` for containerization. The server is designed to handle API requests and serves as the backend for the frontend application. For demo purpose this app will simple expose some static data.
- **Frontend:** Contains a simple application built with a React framework. It interacts with the backend API to fetch the data and render on the page.

## Project Structure

### Backend
Navigate to the `backend` directory and run the following command to start the backend server:

`python main.py`

### Frontend
Navigate to the `frontend` directory and run the following command to start the frontend application: 
`npm run dev`