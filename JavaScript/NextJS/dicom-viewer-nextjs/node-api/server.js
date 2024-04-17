const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const session = require('express-session')
const cors = require('cors')
const authRoute = require('./router/auth')
const app = express();
const port = 5000; // Use a different port than your Next.js app

require('dotenv').config()
require('./db.js')

app.use('/uploads', express.static('uploads'));

app.use(bodyParser.json());
app.use(cookieParser())
app.use(cors({
    origin: ['http://localhost:3001', 'http://127.0.0.1:3001'],
    methods: ['GET', 'POST'],
    credentials: true,
  }));
  // app.use(session({
  //   secret: 'your_secret_key',
  //   resave: false,
  //   saveUninitialized: true,
  //   cookie: { secure: true } // use secure: true in production with HTTPS
  // }));

app.use('/auth', authRoute)

app.get('/api/hello', (req, res) => {
  res.json({ message: 'Hello from Node.js backend!' });
});

app.listen(port, () => {
  console.log(`Node.js API server listening at http://localhost:${port}`);
});
