<script>
	import { json } from "@sveltejs/kit";

    let projects = [
        { name: "Project 1" },
        { name: "Project 2" },
        { name: "Project 3" },
        { name: "Project 4" },
    ];
    if(typeof document != 'undefined') if (!document.cookie.includes('token:')) window.open('/signin', '_self')

    let token = ''
    const init = async () => {
        if(typeof window == 'undefined') return;
        if(!document.cookie.includes('token:')) return;
        token = (document.cookie.split('; ').find(x=>x.includes('token:'))||'').slice(6)

        let response = await fetch('https://d8a8-129-45-112-40.ngrok-free.app/workspaces/me', {
            method: 'get',
            headers: {
                Authorization: 'token ' + token 
            }

        })

        console.log(token)
        console.log(response)
    }

    const create = async () => {
        if(typeof window == 'undefined') return;
        if(!document.cookie.includes('token:')) return;

        let response = fetch('https://d8a8-129-45-112-40.ngrok-free.app/workspaces/create', {
            method: 'post',
            headers: {
                Authorization: 'token ' + token 
            },
            body: JSON.stringify({
                owner_id: ''
            })
        })

    }

    init()
</script>

<main>
    <h2> current project list </h2>
    <div class="container">
        {#each projects as project}
            <div class="card">
                <h3>{project.name}</h3>
                click to edit or view this Project<br>
                <a href="/workspace">edit</a> <a href="/workspace">delete</a>
            </div>
        {/each}
    </div>
    <h2>join or create a new project</h2>
    <div class="container">
        <form>
            <label>
                Project Name:
                <input type="text" />
            </label>
            <button type="submit">Create Project</button>
        </form>
        <form>
            <label>
                Project Name:
                <input type="text" />
            </label>
            <button type="submit">Join Project</button>
        </form>
    </div>
</main>

<style>
    main{
        padding: 10px;
		padding-top: 90px;
        background-image: linear-gradient(45deg, #fff 25%, #fbfbfb 25%, #fbfbfb 50%, #fff 50%, #fff 75%, #fbfbfb 75%, #fbfbfb 100%);
        background-size: 30px 30px;
        height: 100%;
    }
    h2{
        text-decoration: underline;
        margin: 20px 0 10px 0;
    }
    .container{
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        padding: 0 20px;
    }
    .card {
        border: 1px solid #ccc;
        padding: 1rem;
        margin-bottom: 1rem;
        min-width: 300px;
        max-width: 500px;
        flex-grow: 1;
        background-color: white;
        padding-bottom: 50px;
        user-select: none;
        cursor: pointer;
        border-radius: 7px;
    }
    h3{
        margin: 15px 0;
    }
    form{
        display: flex;
        flex-direction: column;
        gap: 1rem;
        max-width: 500px;
        border: 1px solid #ccc;
        padding: 10px;
        background-color: white;
        flex-grow: 1;
        border-radius: 7px;
    }
    label{
        display: flex;
        align-items: center;
        gap: 10px;
    }
    input{
        font-family: var(--font);
        font-size: 1rem;
        border: none;
        border-bottom: solid 1px #ccc;
        transform: translateY(3px);
    }
    input:focus{
        outline: none;
    }
    button{
        border: solid 1px #ccc;
        background-color: white;
        padding: 10px;
        cursor: pointer;
        border-radius: 7px;
    }
</style>
