const { default: mongoose }  = require('mongoose')

const userSchema = new mongoose.Schema({
    username: {
        type: String,
        require: true,
        unique: true,
    },
    password: {
        type: String,
        require: true,
    },
    email: {
        type: String,
        require: true,
        unique: true,
    },
    user_type: {
        type: String, 
    },
}, {timestamps:true})

const User = mongoose.model('users', userSchema)
module.exports = User