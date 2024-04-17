import Image from 'next/image';
import styles from './home.module.css'

const Home = () => {
  return <div className={styles.container}>
    <div className={styles.textContainer}>
      <h1>Creative Thought Agency.</h1>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus accumsan, purus at dictum semper, eros mi facilisis elit, id finibus nulla mi sed purus. Aliquam feugiat pulvinar augue, sit amet finibus justo scelerisque in. Nam a auctor mauris. Nullam id odio id lacus tempor viverra ut vel lorem.</p>
      <div className={styles.buttons}>
        <button className={styles.button}>Learn More</button>
        <button className={styles.button}>Contact</button>
      </div>
      <div className={styles.brands}>
        <Image src="/brands.png" alt='' fill className={styles.brandImg} />
      </div>
    </div>
    <div className={styles.imgContainer}>
      <Image src="/hero.gif" alt='' fill className={styles.heroImg} />
    </div>
  </div>;
};

export default Home;