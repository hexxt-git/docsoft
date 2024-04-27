<script>
    let projects = [
        { name: "Project 1" },
        { name: "Project 2" },
        { name: "Project 3" },
        { name: "Project 4" },
    ];
</script>

<main>
    <h2> current project list </h2>
    <div class="container">
        {#each projects as project}
            <div class="card">
                <h3>{project.name}</h3>
                click to edit or view this project
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
