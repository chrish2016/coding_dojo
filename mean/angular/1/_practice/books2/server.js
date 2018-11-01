const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = process.env.PORT || 8000;

require('./server/config/database');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static(path.resolve('dist/public')));
app.use(require('./server/routes'));




app.listen(port, ()=> console.log('Express server listening on port 8000'));
