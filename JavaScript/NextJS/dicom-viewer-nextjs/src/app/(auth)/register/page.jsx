import Link from "next/link";
import styles from "./register.module.css";
import AuthForm from "../../components/authForm/authForm";

const RegisterPage = () => {
    return (
        <div>
            <AuthForm type="register" />
        </div>
    )
}

export default RegisterPage
