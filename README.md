# Student Job Application Tracker

A web-based job application tracker built with Flask and SQLite to help students manage and monitor their job applications.

## Features

- Add job applications
- Edit existing applications
- Delete applications with confirmation
- Track application status
- Record application dates
- Store job posting URLs
- Add application notes
- Search applications by company or role
- Filter applications by status
- View detailed application information
- Dashboard statistics
- Responsive design

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript

## Application Statuses

- Applied
- Assessment
- Interview
- Offer
- Rejected

## Project Structure

```text
student-job-tracker/
│
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── edit.html
│   └── details.html
│
├── static/
│   └── style.css
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
└── jobs.db