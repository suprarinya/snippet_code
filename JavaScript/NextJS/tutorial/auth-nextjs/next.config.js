/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
        remotePatterns:[
            {
                protocol: 'https',
                // hostname: 'images.unsplash.com',
                hostname: '**',
                port: '',
                pathname: '**',
            }
        ]
    }
}

module.exports = nextConfig
