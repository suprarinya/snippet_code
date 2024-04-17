const moogoose = require('mongoose')

console.log(process.env.MONGODB_URI, 'aa')

moogoose.connect(process.env.MONGODB_URI)
    .then(() => console.log('MongoDB connected...'))
    .catch(err => console.error(err))