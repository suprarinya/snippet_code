export default function handler(req, res) {
    const origin = req.headers.origin;

    // Check if the Origin is one of your allowed origins
    const allowedOrigins = ['http://localhost:3001', 'http://127.0.0.1:3001'];
    if (allowedOrigins.includes(origin)) {
      // Reflect the origin in the CORS header
      res.setHeader('Access-Control-Allow-Origin', origin);
    }
  
    // Include other CORS headers as needed
    res.setHeader('Access-Control-Allow-Methods', 'GET');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    const {imageUrl} = req.query
    console.log('aaaaaaa', imageUrl);
    fetch(imageUrl)
    .then((response) => {
        return response.blob()
    }).then((blob) => {
        blob.arrayBuffer().then((buffer) => {
            const contentType = blob.type
            res.setHeader('Content-Type', contentType)
            res.send(Buffer.from(buffer))
        })
    })
    .catch((err) => {
        console.error('Error fetching image:', err);
        res.status(500).json({error:"Error fetching"})
    })
}