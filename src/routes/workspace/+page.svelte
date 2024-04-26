<script lang="ts">
    import Nav from './Nav.svelte';
    import Canvas from './Canvas.svelte';
    import Inspector from './Inspector.svelte';

</script>

<main>
    <Nav style="grid-column: 1 / -1;" />
    <Canvas />
    <Inspector />
</main>

<style>
    main{
        margin: 0;
        width: 100%;
        height: 100%;
        display: grid;
        grid-template-rows: 70px 1fr;
        grid-template-columns: 1fr 400px;
    }
</style>