CREATE DATABASE resume_db;

USE resume_db;

CREATE TABLE resumes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    phone VARCHAR(20),
    skills TEXT,
    score INT,
    job_role VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
