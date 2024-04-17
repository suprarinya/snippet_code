"use client"

import Link from "next/link"
import styles from "./links.module.css"
import NavLink from "./NavLink/NavLink"
import { useState } from "react"
import Image from "next/image"
import { handleLogout } from "../../../../lib/action"

const Links = ({session}) => {
    const links = [
        {
            title: "Homepage",
            path: "/",
        },
        {
            title: "About",
            path: "/about",
        },
        {
            title: "Contact",
            path: "/contact",
        },
        {
            title: "Blog",
            path: "/blog",
        },
    ]

    const [open, setOpen] = useState(false)

    // TEMPORARY
    // const session = true
    const isAdmin = true

    return (
        <div className={styles.container}>
            <div className={styles.links}>
                {links.map((link) => (
                    <NavLink item={link} key={link.title}></NavLink>
                ))}
                {
                    session?.user ? (
                        <>
                            {session.user?.isAdmin && (
                                <NavLink item={{title:"Admin", path:"/admin"}}></NavLink>
                            )}
                            <form action={handleLogout}>
                                <button className={styles.logout}>Logout</button>
                            </form>     
                        </>
                    ) : (
                        <NavLink item={{title:"Login", path:"/login"}}></NavLink>
                    )
                }
            </div>
            <Image className={styles.menuButton} 
                src="/menu.png"
                alt=""
                width={30}
                height={30}
                onClick={() => setOpen((prev) => !prev)} />
            {open && (
                <div className={styles.mobileLinks}>
                    {links.map((link) => (
                        <NavLink item={link} key={link.title}></NavLink>
                    ))}
                </div>
            )}
        </div>
    )
}

export default Links;