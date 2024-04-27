<script>
	import { writable } from 'svelte/store';
    import Canvas from './Canvas.svelte';
    import Inspector from './Inspector.svelte';

    const inspected = writable({})
</script>

<main>
    <Canvas {inspected}/>
    <Inspector {inspected} />
</main>

<style>
    main{
        margin: 0;
        width: 100%;
        height: 100%;
        display: grid;
    }
</style>