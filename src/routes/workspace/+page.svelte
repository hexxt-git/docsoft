<script lang="ts">
    import Nav from './Nav.svelte';
    import Canvas from './Canvas.svelte';
    import Inspector from './Inspector.svelte';

</script>

<main>
    <Nav />
    <Canvas />
    <Inspector />
</main>

<style>
    main{
        margin: 0;
        width: 100%;
        height: 100%;
        display: grid;
    }
</style>