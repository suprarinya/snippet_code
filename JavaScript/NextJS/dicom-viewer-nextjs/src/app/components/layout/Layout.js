const { default: Footer } = require("../footer/Footer")
const { default: Header } = require("../header/Header")
const styles = require("./layout.module.css")

const Layout = ({children}) => {
    return (
        <>
            <Header />
                <main className={styles.main_content}>{children}</main>
            <Footer className={styles.fixed_footer} />
        </>
    )
}

export default Layout