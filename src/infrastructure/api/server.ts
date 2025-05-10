import express from 'express';
import axios from 'axios';
import path from 'path';
import { fileURLToPath } from 'url';
import rateLimit from 'express-rate-limit';

const app = express();
const port = 3000;

// Fix for __dirname in ES module
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname)));

// Configure rate limiter for the root URL
const rootLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
});

// Serve index.html on the root URL
app.get('/', rootLimiter, (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Endpoint to simulate dice roll with animation
app.get('/roll-dice', async (req, res) => {
  const rollDice = () => Math.floor(Math.random() * 6) + 1;
  const animationFrames = 10;
  const interval = 100; // milliseconds

  let frame = 0;
  const intervalId = setInterval(() => {
    if (frame < animationFrames) {
      const diceRoll = rollDice();
      res.write(`data: {"rolling": true, "result": ${diceRoll}}

`);
      frame++;
    } else {
      clearInterval(intervalId);
      const finalRoll = rollDice();
      res.write(`data: {"rolling": false, "result": ${finalRoll}}

`);
      res.end();
    }
  }, interval);

  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
}); 