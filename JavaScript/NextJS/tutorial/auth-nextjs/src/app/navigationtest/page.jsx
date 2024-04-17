"use client" // when using event, should be client
import Link from "next/link"
import { usePathname, useRouter, useSearchParams } from "next/navigation"

const NavigationTestPage = () => {

    // client side navigation
    const router = useRouter()
    const pathname = usePathname()
    const searchParams = useSearchParams()

    const q = searchParams.get("q")

    console.log(pathname);
    console.log(q);

    const handleClick = () => {
        console.log('clicked');
        // router.push("/") // add directory to top of stack
        router.replace('/') // not add directory to stack
        // router.refresh() // for refresh data
        // router.back() // back to previous page
        // router.forward() 
    }

    return (
        <div>
            <Link href='/' prefetch={false}>Click here</Link>
            <button onClick={handleClick}>Write and Redirect</button>
        </div>
    )
}

export default NavigationTestPage