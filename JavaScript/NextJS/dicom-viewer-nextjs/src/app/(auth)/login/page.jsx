import Link from "next/link";
import styles from "./login.module.css";
import AuthForm from "../../components/authForm/authForm";

const LoginPage = () => {
    return (
        <div>
            <AuthForm type="login" />
        </div>
    )
}

export default LoginPage
