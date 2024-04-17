"use client"
import Link from "next/link"
import { useRouter } from "next/navigation";


const Header = () => {
    const router = useRouter()

    const handleLogout  = async () => {
        const url = `${process.env.NEXT_PUBLIC_NODE_URI}/auth/logout`
        localStorage.removeItem('userdata')
        document.cookie = 'userdata=; Path=/; Max-Age=0;';
        router.push('/login')
    }

    return (
        <header style={{background: '#0d0c22', padding: '20px 0'}}>
            <nav style={{width: '80%', margin: '0 auto', display: 'flex', justifyContent: 'space-between'}}>
            <Link href="/">
                <p>Home</p>
            </Link>
            <Link href="/upload">
                <p>Upload</p>
            </Link>
            <Link href="/viewer">
                <p>Viewer</p>
            </Link>
            <Link href="/about">
                <p>About</p>
            </Link>
            <Link href="#">
                <p onClick={ handleLogout }>Logout</p>
            </Link>
            </nav>
        </header>
    )
}

export default Header