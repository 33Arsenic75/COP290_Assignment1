const express = require('express');
const sqlite3 = require('sqlite3');

const app = express();
const port = 3000;

app.use(express.static('public'));
app.use(express.json());

app.get('/data', (req, res) => {
  const startDate = req.query.startDate;
  const endDate = req.query.endDate;
  const stock = req.query.stock;
  /// console.log(stock)
  const dbPath = `historical_data/${stock}.db`;
  const query = `
    SELECT DATE(DATE) as date,CLOSE FROM stock_data_table
    WHERE date BETWEEN ? AND ?
  `;
  const db = new sqlite3.Database(dbPath, (err)=>{
  db.all(query, [startDate, endDate], (err, rows) => {
    /// console.log(query)
    if (err) {
      /// console.error(err);
      res.status(500).json({ error: 'Internal Server Error' });
    } else {
      console.log(rows)
      res.json(rows);
    }
  });
  db.close()
  });
});

// Serve the HTML file on the root path
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
