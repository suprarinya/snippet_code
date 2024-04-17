const express = require('express');
const router = express.Router()

router.use((req, res, next) => {
    console.log('Home: ', Date.now());
    next()
})

router.get('/', (req, res) => {
    const getcookie = res.cookie.userdata
    console.log(getcookie);
})



module.exports = router