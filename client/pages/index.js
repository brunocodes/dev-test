import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <>
    <nav className={styles.nav}>
      <ul>
        <li>
          <Link href='/'>Home</Link>
        </li>
      </ul>
      <Link href='/signup'><button>Registrar</button></Link>  
    </nav>
    <div className={styles.container}>
      <Head>
        <title>Brunocodes Dev test</title>
        <meta name="description" content="Brunocodes Dev test with Next.js" />
        <link rel="icon" href="/favicon.ico" />
      </Head>


      <main className={styles.main}>
        <h2 className={styles.title}>
          Brunocodes Dev test with Next.js!
        </h2>

        <p className={styles.description}>
          Dev test information
        </p>

        <div className={styles.grid}>
          <a href="https://github.com/brunocodes/dev-test" className={styles.card}>
            <h2>Documentação &rarr;</h2>
            <p>Mais informações no github README.</p>
          </a>
        </div>
      </main>

      <footer className={styles.footer}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{' '}
          <span className={styles.logo}>
            <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />
          </span>
        </a>
      </footer>
    </div>
    </>
  )
}
