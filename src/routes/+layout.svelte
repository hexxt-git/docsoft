<script>
    import Nav from './Nav.svelte';
</script>

<Nav />
<slot />

<style>
    :global(body){
        margin: 0;
        height: 100vh;
        width: 100vw;
        overflow: hidden;
        font-family: 'Inter', sans-serif;
        background-color: white;
        color: #404046;
    }
    :global(*){
        --font: 'Inter', sans-serif;
        --accent: #1dcceb;
        --color: #404046;
        --background: white;
        --node-color: #0f0f28;
        --node-shadow: #202432;
    }
</style>