const express = require("express");
const cors = require("cors");
const fs = require("fs");

const app = express();
app.use(cors());

// Load quotes
const quotes = JSON.parse(fs.readFileSync("quotes.json", "utf-8"));

// GET all quotes
app.get("/quotes", (req, res) => {
  res.json(quotes);
});

// GET one random quote
app.get("/quotes/random", (req, res) => {
  const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
  res.json({ quote: randomQuote });
});

// GET search
app.get("/quotes/search", (req, res) => {
  const query = req.query.q?.toLowerCase();
  if (!query) return res.status(400).json({ error: "Missing query param `q`" });

  const results = quotes.filter((q) => q.toLowerCase().includes(query));
  res.json(results);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`✅ Naval API running at http://localhost:${PORT}`);
});
