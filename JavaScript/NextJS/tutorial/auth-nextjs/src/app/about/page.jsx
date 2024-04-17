import Image from "next/image";
import styles from "./about.module.css"

export const metadata = {
    title: 'About Page',
    description: 'About description',
}

const AboutPage = () => {
    // console.log('lets check where');
    return (
        <div className={styles.container}>
            {/* <div className={styles.imgContainer}>
            <Image src="/about.png" alt="about" fill/>
            <Image src="https://images.unsplash.com/photo-1644245991167-b1f5202e8211?q=80&w=1287&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="about" fill/>
            </div> */}
            <div className={styles.textContainer}>
                <h2 className={styles.subtitle}>About Agency</h2>
                <h1 className={styles.title}>We create digitals idea that are bigger. bolder, braver and better</h1>
                <p className={styles.desc}>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum </p>
                
                <div className={styles.boxes}>
                    <div className={styles.box}>
                        <h1>10 K+</h1>
                        <p>Years of experience</p>
                    </div>
                    <div className={styles.box}>
                        <h1>10 K+</h1>
                        <p>Years of experience</p>
                    </div>
                    <div className={styles.box}>
                        <h1>10 K+</h1>
                        <p>Years of experience</p>
                    </div>
                </div>

            </div>
            <div className={styles.imgContainer}>
                <Image
                src="/about.png"
                alt="About Image"
                fill
                />
            </div>
        </div>
    )
}

export default AboutPage;