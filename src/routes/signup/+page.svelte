<script>
    let first_name = '123@123';
    let last_name = '123@123';
    let email = '123@123';
    let company_name = '123@123';
    let password = '123@123';

    async function signUp() {
        let response;
        try{
            response = await fetch('https://d8a8-129-45-112-40.ngrok-free.app/auth/signup/', {
            method: 'post',
            body: JSON.stringify({
                first_name,
                last_name,
                email,
                company_name,
                password
            }),
        })} catch (err) {
            console.error(err)
        }

        if(response?.ok) {
            alert('signup successfull')
            window.open('/signin', '_self')
        }
    }
</script>

<main>
    <h1>Sign Up</h1>
    <form on:submit|preventDefault={signUp}>
        <label>
            First Name:
            <input type="text" bind:value={first_name} required />
        </label>
        <label>
            Last Name:
            <input type="text" bind:value={last_name} required />
        </label>
        <label>
            Company Name:
            <input type="text" bind:value={company_name} required />
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
