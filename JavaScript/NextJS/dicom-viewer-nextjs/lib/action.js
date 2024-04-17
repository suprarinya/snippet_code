const jwt = require('jsonwebtoken')
const cookie = require('cookie')

const checkAuthentication = (req) => {
    const cookies = req.headers.cookie
    const parsedCookies  = cookie.parse(cookies || '')
    const token = parsedCookies.userdata

    if (!token) return false;
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET)
        return true
    } catch(err){
        console.error(err);
        return false
    }
}


module.exports = {checkAuthentication}
