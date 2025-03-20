const express = require('express');
const mysql = require('mysql');
const path = require('path');
const app = express();
const PORT = 3000;

// Serve static files from frontend folder
app.use(express.static(path.join(__dirname, '..', 'frontend')));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// MySQL connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '3012',
  database: 'resume_db'
});

db.connect(err => {
  if (err) throw err;
  console.log('✅ Connected to MySQL');
});

// API route
app.get('/resumes', (req, res) => {
  db.query('SELECT * FROM resumes ORDER BY score DESC', (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});

// Homepage route
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'frontend', 'index.html'));
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 Server running at http://localhost:${PORT}`);
});
