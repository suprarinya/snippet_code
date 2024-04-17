"use client"
import Link from "next/link";
import styles from "./authForm.module.css";
import { useState } from "react";
import { useRouter } from "next/navigation"



const AuthForm = ({type}) => {
    const router = useRouter()
    const [errormessage, setErrorMessage] = useState('')

    const handleSubmit = async (e) => {
        e.preventDefault()

        let formData = {}
        if(type == 'login'){
            formData = {
                username: e.target.username.value,
                password: e.target.password.value,
            }
        } else {
            formData = {
                username: e.target.username.value,
                password: e.target.password.value,
                email:    e.target.email.value,
                re_password: e.target.re_password.value,
            }
        }


        let url = `${process.env.NEXT_PUBLIC_NODE_URI}/auth/${type}`
        const res = await fetch(url, {
            credentials: 'include',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body:JSON.stringify(formData),
        })

        const json = await res.json()
        if(res.ok) {
            const successmessage = json.success
            localStorage.setItem('userdata', successmessage)
            // document.cookie = `userdata=${localStorage.getItem('userdata')};SameSite=Lax; path=/;`;
            document.cookie = `userdata=${successmessage};SameSite=Lax; path=/; Secure; Max-Age=${process.env.NEXT_PUBLIC_JWT_EXPIRES_IN};`
            console.log(successmessage, successmessage == 'home');
            if(successmessage){
                router.push('/')
            } else {
                router.push('/login')
            }
        } else {
            const errormessage = json.error
            setErrorMessage(errormessage)
        }
    }

    return (
        <div className={styles.container} onSubmit={handleSubmit}>
            <form className={styles.form}>
                <h2>{type == 'login' ? 'Login' : 'Register'}</h2>
                {
                    type == 'register' && (
                        <div className={styles.formControl}>
                            <label >Email</label>
                            <input type="text" id="email" name="email" required />
                        </div>
                    )
                }
                <div className={styles.formControl}>
                    <label >Username</label>
                    <input type="text" id="username" name="username" required />
                </div>
                <div className={styles.formControl}>
                    <label >Password</label>
                    <input type="password" id="password" name="password" required />
                </div>
                {
                    type == 'register' && (
                        <div className={styles.formControl}>
                            <label >Repeat Password</label>
                            <input type="password" id="re_password" name="re_password" required />
                        </div>
                    )
                }
                {
                    errormessage && (
                        <div className="alert alert-danger" role="alert">
                            {errormessage}
                        </div>
                    )
                }
                <button className={styles.loginBtn} type="submit">{type == 'login' ? 'Login' : 'Save'}</button>
                <Link className={styles.backBtn} href={type == 'login' ? '/register' : '/login'}>{type == 'login' ? 'Register' : 'Back'}</Link>
            </form>
        </div>
    )
}

export default AuthForm
