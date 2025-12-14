# Sweet Shop Management System

## Project Description
Full-stack Sweet Shop Management System with authentication,
inventory management, and role-based access.

## Tech Stack
- Backend: FastAPI, SQLite
- Frontend: React
- Auth: JWT
- Testing: Pytest

## How to Run Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

## How to Run Frontend
cd frontend
npm install
npm start

## API Endpoints
- POST /api/auth/register
- POST /api/auth/login
- GET /api/sweets
- POST /api/sweets
- POST /api/sweets/{id}/purchase
- POST /api/sweets/{id}/restock

## Screenshots
(Add screenshots of frontend + backend running)

## My AI Usage
I used ChatGPT to:
- Design backend architecture
- Generate FastAPI boilerplate
- Write Pytest test cases
- Debug frontend-backend integration

AI helped speed up development,
but all logic and final decisions were implemented by me.
