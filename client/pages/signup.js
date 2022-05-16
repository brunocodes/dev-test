import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import styles from '../styles/Home.module.css'
import { useState } from "react";

export default function Signup() {
  const [submited, setSubmit] = useState(false);
  const [clear, setClear] = useState(false);
  const submitUser = async (event) => {
    event.preventDefault();

    const newUser = {
      "user_id": 0,
      "nome": event.target.nome.value,
      "email": event.target.email.value,
      "telefone": event.target.telefone.value,
      "endereco": event.target.endereco.value,
      "profissao": event.target.profissao.value
    };
    
    fetch("http://127.0.0.1:8000/users", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        newUser
      })
      
    }).then((response) => {
      console.log(newUser)
      if (response.status === 201 || response.status === 200) return response.json();
      // console.log(response)
      // throw new Error("Failed to add user");

    }).then((jsonRes) => {
      setSubmit(true);
      alert(`Obrigado pelo seu cadastro ${event.target.nome.value}`);
    })
  };
  const submitClear = async (event) => {
    event.preventDefault();
    setClear(true);
  }
  return (
    <>
    <nav className={styles.nav}>
      <ul>
        <li><Link href="/">Home</Link></li>
        <Link href="/#"><button>signup</button></Link>  
      </ul>
    </nav>
    <div className={styles.container}>
      <Head>
        <title>Cadastro</title>
        <meta name="description" content="Cadastro de usuário" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.description}>
          Cadastrar!
        </h1>
        <div>

          <form onSubmit={submitUser}>
            <label for="nome">Nome Completo</label><br />
            <input type="text" id="nome" name="nome" /><br />

            <label for="email">Email:</label><br />
            <input type="text" id="email" name="email" /><br />

            <label for="telefone">Telefone:</label><br />
            <input type="text" id="telefone" name="telefone" /><br />

            <label for="endereco">Endereço:</label><br />
            <input type="text" id="endereco" name="endereco" /><br />

            <label for="profissao">Profissão:</label><br />
            <input type="text" id="profissao" name="profissao" /><br />

            <label for="avatar">Upload de Curriculo:</label><br /><br />
            <input type="file" id="curriculo" name="curriculo" accept="application/pdf"></input><br /><br />

            <input type="reset" value="Limpar"></input>
            <button>Enviar</button>
          </form>
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
