<script>
    let firstName = '';
    let lastName = '';
    let email = '';
    let password = '';

    function signUp() {
        // Perform sign-up logic here
        console.log('Signing up...');
        console.log('First Name:', firstName);
        console.log('Last Name:', lastName);
        console.log('Email:', email);
        console.log('Password:', password);
        window.open('/workspace', '_self');
    }
</script>

<main>
    <h1>Sign Up</h1>
    <form on:submit|preventDefault={signUp}>
        <label>
            First Name:
            <input type="text" bind:value={firstName} required />
        </label>
        <label>
            Last Name:
            <input type="text" bind:value={lastName} required />
        </label>
        <label>
            Email:
            <input type="email" bind:value={email} required />
        </label>
        <label>
            Password:
            <input type="password" bind:value={password} required />
        </label>
        <button type="submit">Sign Up</button>
    </form>

    <p>Already have an account? <a href="/signin">Sign in</a></p>

    <div id='wip'>this page is a work in progress*</div>
</main>

<style>
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        background-image: linear-gradient(45deg, #fff 25%, #fbfbfb 25%, #fbfbfb 50%, #fff 50%, #fff 75%, #fbfbfb 75%, #fbfbfb 100%);
        background-size: 30px 30px;
    }

    h1 {
        margin-bottom: 1rem;
        font-size: 2rem;
        color: #333;
    }

    form {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        background-color: #f5f5f5;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    }

    label {
        display: flex;
        flex-direction: column;
        font-size: 1rem;
        color: #333;
    }

    input {
        padding: 0.5rem;
        border-radius: 4px;
        border: 1px solid #ccc;
        font-size: 1rem;
        color: #333;
    }
    input:focus {
        outline: none;
        border-color: var(--accent);
    }

    button {
        padding: 0.5rem 1rem;
        border-radius: 4px;
        border: none;
        background-color: var(--accent);
        color: #fff;
        cursor: pointer;
        font-size: 1rem;
        font-weight: bold;
        text-transform: uppercase;
    }
    #wip {
        position: fixed;
        bottom: 0;
        right: 0;
        margin: 5px 10px;
    }
</style>
