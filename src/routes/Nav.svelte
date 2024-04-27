<script>
	import { page } from '$app/stores';
	export let style = '';
	let query = '';
	const search = () => {
		console.log(query);
	};
</script>

<nav {style}>
	<a href="/" id="logo">
		<img src="/favicon.png" alt="dock soft logos" />
		DocSoft
	</a>
	{#if $page.url.toString().includes('/workspace')}
		<form on:submit|preventDefault={search}>
			<textarea
				name="search"
				id="searchbar"
				placeholder="AI powered search"
				rows="1"
				cols="25"
				bind:value={query}
			></textarea>
			<button><img src="/search.svg" alt="search" class="icon" /></button>
		</form>
	{/if}
	<div id="links">
        {#if typeof document != 'undefined'}
            <a href="/projects">
                <img src="/settings.svg" alt="settings" class="icon" />
            </a>
            <a href="/help">
                <img src="/help.svg" alt="help" class="icon" />
            </a>
            <a href={!document.cookie.includes('token:') ? 'signin' : 'projects'}>
                <img src="/profile.svg" alt="profile" class="icon" />
            </a>
        {/if}
	</div>
</nav>

<style>
	nav {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 0 45px 0 20px;
		box-shadow: #0000002f 0 2px 15px;
		z-index: 10;
		margin: 5px;
		border-radius: 10px;
		position: fixed;
		top: 0;
		left: 0;
		width: calc(100% - 10px);
		height: 70px;
		box-sizing: border-box;
		background-color: white;
	}
	#logo {
		height: 100%;
		display: flex;
		align-items: center;
		gap: 10px;
		text-decoration: none;
		color: #404046;
		font-size: 22px;
		font-weight: 600;
		user-select: none;
	}
	#logo img {
		height: 43px;
	}
	form {
		display: flex;
		align-items: center;
		border-radius: 5px;
		background-color: #f2f2f2;
		gap: 5px;
		padding: 0 10px;
	}
	textarea {
		border: none;
		padding: 7px 0;
		font-size: 1.2em;
		box-sizing: border-box;
		resize: none;
		overflow-y: hidden;
		font-family: Arial, Helvetica, sans-serif;
		background: transparent;
	}
	textarea:focus {
		outline: none;
	}
	textarea::placeholder {
		color: #9e9e9e;
	}
	form button {
		background: transparent;
		border: none;
		padding: 0;
		cursor: pointer;
	}
	.icon {
		filter: invert(0.4);
	}
	form img {
		height: 22px;
		filter: invert(0.4);
		transition: filter 100ms ease-in-out;
	}
	form button:hover img {
		filter: invert(0.55);
	}
	#links {
		display: flex;
		align-items: center;
		gap: 20px;
	}
</style>
