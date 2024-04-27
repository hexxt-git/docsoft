<main>
    <img src="/favicon.png" alt="logo">
    <h1>Welcome to our Document Management System</h1>
    <p>
        If you are new here, please <a href="/signup">sign up</a> or <a href="/signin">sign in</a> to get started.
    </p>
    <p>
        If you already have an account, you can access your <a href="/projects">projects</a> here.
    </p>
    <div id="wip">
        this website is still a work in progress but all the main functionality is working<br>
        you can access the workspace on /workspace it currently only has testing data. you can test the backend and search engine in their respective directories<br>
        
    </div>
</main>

<style>
    main {
        padding-top: 90px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }

    h1 {
        font-size: 2rem;
        color: #333;
        margin-bottom: 1rem;
    }

    p {
        text-align: center;
        margin-bottom: 0.5rem;
    }

    a {
        color: #007bff;
        text-decoration: none;
    }

    img{
        height: 130px;
        width: 130px;
    }
    #wip {
        position: fixed;
        bottom: 0;
        right: 0;
        margin: 5px 10px;
        max-width: 400px;
        color: #666;
    }
</style>