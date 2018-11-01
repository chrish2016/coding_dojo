var express = require('express');
var app = express();
var path = require('path');
var mongoose = require('mongoose');
var bodyParser = require('body-parser');
var morgan = require('morgan');
var port = process.eventNames.PORT || 8080;

var User = require('./app/models/user');

mongoose.connect('mongodb://localhost/awesome_test', { useCreateIndex: true, useNewUrlParser: true });

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(function(req, res, next){
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type, \
    Authorization');
    next();
});
app.use(morgan('dev'));

app.get('/', function(req, res){
    res.send('Welcome to the HOME PAGE!');
});

var User = require('./app/models/user');

var apiRouter = express.Router();

apiRouter.use(function(req, res, next){
    console.log('Somebody just came to our app!');
    next();
});

apiRouter.get('/', function(req, res){
    res.json({ message: 'horray! welcome to our api!' });
});

apiRouter.get('/users')
    .post(function(req, res){
        var user = new User();
        user.name = req.body.name;
        user.username = req.body.username;
        user.password = req.body.password;
        user.save(function(err){
            if(err){
                if(err.code == 11000)
                return res.json({ success: false, message: 'A user with that username already exists.' });
                else
                    return res.send(err);
            }
            res.json({ message: 'User created! '});
        });
    })


    apiRouter.route('/users')
     // create a user (accessed at POST http://localhost:8080/api/users)
    .post(function(req, res) {
    
    // create a new instance of the User model
    var user = new User();
    
    // set the users information (comes from the request)
    user.name = req.body.name;
    user.username = req.body.username;
    user.password = req.body.password;
    
    // save the user and check for errors
    user.save(function(err) {
        if (err) {
            // duplicate entry
            if (err.code == 11000)
                return res.json({ success: false, message: 'A user with that username already exists. '});
            else
                return res.send(err);
            }
    
        res.json({ message: 'User created!' });
        });
    
    })

app.use('/api', apiRouter);

app.listen(port);
console.log('Magic happens on port ' + port);