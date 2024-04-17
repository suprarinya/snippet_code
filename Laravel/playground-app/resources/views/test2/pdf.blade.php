<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>




    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.5.3/jspdf.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.6/jspdf.plugin.autotable.min.js"></script>
    <script>
        /*
        |--------------------------------------------------------------------------
        | Below is some helper functions for the examples
        |--------------------------------------------------------------------------
        */

        function headRows() {
            return [
                { id: 'ID', name: 'Name', email: 'Email', city: 'City', expenses: 'Sum' },
            ]
        }

        function footRows() {
            return [
                { id: 'ID', name: 'Name', email: 'Email', city: 'City', expenses: 'Sum' },
            ]
        }

        function columns() {
            return [
                { header: 'ID', dataKey: 'id' },
                { header: 'Name', dataKey: 'name' },
                { header: 'Email', dataKey: 'email' },
                { header: 'City', dataKey: 'city' },
                { header: 'Exp', dataKey: 'expenses' },
            ]
        }

        function data(rowCount) {
            rowCount = rowCount || 10
            var body = []
            for (var j = 1; j <= rowCount; j++) {
                body.push({
                id: j,
                name: faker.name.findName(),
                email: faker.internet.email(),
                city: faker.address.city(),
                expenses: faker.finance.amount(),
                })
            }
            return body
        }

        function bodyRows(rowCount) {
            rowCount = rowCount || 10
            var body = []
            for (var j = 1; j <= rowCount; j++) {
                body.push({
                id: j,
                name: faker.name.findName(),
                email: faker.internet.email(),
                city: faker.address.city(),
                expenses: faker.finance.amount(),
                })
            }
            return body
        }
    </script>
    <script>
        var doc = new jsPDF('l')

    </script>
</body>
</html>