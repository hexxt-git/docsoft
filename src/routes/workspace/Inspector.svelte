<script>
	import { writable } from "svelte/store";

	export let inspected = writable({})

    
</script>

<nav>
    <h1>Selected</h1>
    <h2><span>name:</span> project_plan</h2>
    <h2><span>type:</span> application/vnd.ms-excel</h2>
    <h2><span>Location:</span> /root/projects</h2>
    <h2><span>Last modified:</span> 10-Aug-2023 <span>By:</span> John</h2>
    <h2><span>size on disc:</span> 2.75Mb</h2>
    <hr>
    <h1>File Permissions</h1>
    <h2><span>Owner:</span> John</h2>
    <h2><span>Group:</span> Projects</h2>
    <h2><span>Others:</span> Read</h2>
    <hr>
    <h1>Notes</h1>
    <p>This file contains the project plan for Q4.</p>
    <hr>
    <h1>File Actions</h1>
    <li>download</li>
    <li>share</li>
    <li>convert</li>
    <li>delete</li>
    <li>rename</li>
</nav>

<style>
    nav{
        background-color: white;
        height: calc(100% - 105px);
        width: 400px;
        position: fixed;
        top: 80px;
        right: 5px;
        box-shadow: #00000025 -2px 0 15px;
        padding: 10px;
        border-radius: 10px;
        z-index: 11;
        overflow-y: auto;
        scrollbar-width: thin;
    }
    h1{
        font-size: 16px;
        font-weight: 400;
        margin: 0;
    }
    h2 span{
        font-weight: 400;
        color: #111;
    }
    h2{
        margin: 0 5px;
        font-size: 18px;
        font-weight: 500;
    }
    hr{
        margin-top: 15px;
        margin-bottom: 10px;
    }
    li{
        list-style: none;
        padding: 10px;
        background-color: #f6f6f6;
        margin: 5px 0;
        border-radius: 5px;
        cursor: pointer;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    li:hover{
        background-color: #f9f9f9;
    }
    p{
        background-color: #f5f5f5;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
        font-weight: 500;
    }
</style>
