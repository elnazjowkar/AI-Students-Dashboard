const express = require('express');
const fs = require('fs');
const csv = require('csv-parser');
const cors = require('cors');

const app = express();
app.use(cors());

let results = [];

fs.createReadStream('./AI_Impact_Student_Life_2026.csv')
    .pipe(csv())
    .on('data', (data) => results.push(data))
    .on('end', () => {
        console.log('CSV Loaded');
    });

app.get('/data', (req, res) => {
    res.json(results);
});

app.listen(3000, () => console.log('Server running on 3000'));