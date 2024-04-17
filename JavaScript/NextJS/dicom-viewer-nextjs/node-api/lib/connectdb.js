const User = require("../models/user")

const findOneInTable = async (type, where) => {
    /* find only one row from table */
    let findone = {}
    if(type == 'user'){
        findone = await User.findOne(where)

    }
    return findone
}

module.exports = {findOneInTable}