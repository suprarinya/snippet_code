
import Image from "next/image";
import styles from "./page.module.css";
import Layout from "./components/layout/Layout";
// import {checkAuthentication} from '../../lib/action'

const Home = () => {
  

  return (
    <Layout>
      <div style={{width: '80%', margin: '20px auto'}}>
        <h1>Welcome to My Website</h1>
        <p>This is a simple example of a Next.js application using a Header and Footer layout.</p>
        {/* <button onClick={ handleLogout } type="button">Logout</button> */}
      </div>
    </Layout>
    
  );
}

export default Home

