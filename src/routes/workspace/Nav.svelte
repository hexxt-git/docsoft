<script lang="ts">
    export let style: string = ''
</script>

<nav style={style}>
    <div id="logo">Logo</div>
    <div id="location">/root/folder</div>
    <div id="user">U</div>
</nav>

<style>
    nav{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 45px 0 30px;
        border-bottom: solid white 1px;
    }
</style>