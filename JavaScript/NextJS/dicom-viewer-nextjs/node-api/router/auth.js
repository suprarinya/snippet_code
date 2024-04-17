const express = require('express');
const User = require('../models/user');
const router = express.Router()
const bcrypt = require('bcrypt')
const jwt = require('jsonwebtoken')
const { findOneInTable } = require("../lib/connectdb.js")

router.use((req, res, next) => {
    console.log('Auth: ', Date.now());
    console.log('Incoming cookies: ', req.cookies);
    next()
})

router.post('/login', async (req, res) => {
    try {
        const { username, password } = req.body
        const isuser = await findOneInTable('user', {username:username})
        if(isuser){
            const issame = await bcrypt.compare(password, isuser.password)
            if(issame){
                console.log('this is a secret', process.env.JWT_SECRET);
                const token = jwt.sign({name:isuser.username, id:isuser._id.toString()}, process.env.JWT_SECRET, {
                    expiresIn: parseInt(process.env.JWT_EXPIRES_IN),
                })
                // console.log(process.env.JWT_SECRET, process.env.JWT_EXPIRES_IN);
                // res.cookie('userdata', token, {
                //     httpOnly:true,
                //     maxAge:parseInt(process.env.COOKIE_TIME),
                //     sameSite: 'None', // Use 'None' for cross-site cookie use
                //     secure: true, // Required when sameSite is 'None'
                // })
                // req.session.username = isuser.username;
                res.status(201).json({ success:token });
            } else {
                res.status(400).json({ error: 'Error logging in' });
            }
        } else {
            res.status(400).json({error:"There's no user in our system"})
        }
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Error logging in' });
    }
})

router.post('/register', async (req, res) => {
    try {
        const { username, password, email, re_password } = req.body
        if(password !== re_password){
            res.status(400).json({error:"Password do not match"})
        }
        const hashpassword = await bcrypt.hash(password, 10)
        const user = new User({ 
            username:username, 
            password:hashpassword,
            email: email 
        });
        await user.save(); 
        res.status(201).json({ success: 'login' });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Error creating user' });
    }
})

router.post('/logout', (req, res) => {
    try {
        console.log('logout');
        res.cookie('userdata', '', { expires: new Date(0), path: '/', httpOnly: true, secure: true });
    } catch (err) {console.log(err);}
})

module.exports = router

