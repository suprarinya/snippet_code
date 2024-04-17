const express = require('express')
const router = express.Router()

router.use((req, res, next) => {
    console.log('Time: ', Date.now());
    next()
})

router.get('/api/users', (req, res) => {
    
})

module.exports = router