import Link from "next/link";
import styles from "./navbar.module.css"
import Links from "./links/Links";
import { auth, signOut } from "../../../lib/auth";


// export const handleLogout = async () => {
//     "use server"
//     await signOut()
// }

const Navbar = async () => {
    const session = await auth()
    // console.log(session,'Navbar');

    return (
        <div className={styles.container}>
            <Link href="/" className={styles.logo}>Logo</Link>
            <div>
                <Links session={session}/>
            </div>
        </div>
    )
}

export default Navbar;