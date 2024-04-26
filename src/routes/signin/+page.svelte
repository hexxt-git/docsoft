<script>
  let email = '';
  let password = '';

  function signIn() {
    // Perform sign-in logic here
    console.log('Signing in...');
    console.log('Email:', email);
    console.log('Password:', password);
    window.open('/workspace', '_self')
  }
</script>

<main>
  <h1>Sign In</h1>
  <form on:submit|preventDefault={signIn}>

    <label>
      Email:
      <input type="email" bind:value={email} required />
    </label>
    <label>
      Password:
      <input type="password" bind:value={password} required />
    </label>
    <button type="submit">Sign In</button>
  </form>
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }

  h1 {
    margin-bottom: 1rem;
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    background-color: #a8d2ff;
    padding: 15px;
    border-radius: 10px;
  }

  label {
    display: flex;
    flex-direction: column;
  }

  input {
    padding: 0.5rem;
    border-radius: 4px;
    border: 1px solid #ccc;
  }

  button {
    padding: 0.5rem 1rem;
    border-radius: 4px;
    border: none;
    background-color: #007bff;
    color: #fff;
    cursor: pointer;
  }
</style>
