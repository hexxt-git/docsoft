<script lang="ts">
	import { writable } from "svelte/store";

	export let inspected: any = writable({})

    let fakedata: {type: string, location: string, last_modified: string, size: string, owner: string, group: string, notes: Array<string>};

    let old = ''
    inspected.subscribe((newf) => {
        if(newf.name == old) return;
        old = newf.name
        
        fakedata = {
            type: ['image/png', 'file/pdf', 'video/mp4', 'video/mkv', 'game/exe'][Math.random()*5|0],
            location: ['/root/projects', '/root/documents', '/root/files', '/root/images', '/root/videos'][Math.random()*5|0],
            last_modified: ['10-Aug-2023', '15-Sep-2023', '20-Oct-2023', '25-Nov-2023', '30-Dec-2023'][Math.random()*5|0],
            size: ['2.75Mb', '1.5Mb', '3.2Mb', '4.8Mb', '5.6Mb'][Math.random()*5|0],
            owner: ['John', 'Jane', 'Mike', 'Sarah', 'David'][Math.random()*5|0],
            group: ['Projects', 'Documents', 'Files', 'Images', 'Videos'][Math.random()*5|0],
            notes: [
                'This file contains the project plan for Q4.',
                'This file contains important financial data.',
                'This file is for internal use only.',
                'This file contains sensitive information.',
                'This file is part of the marketing campaign.'
            ][Math.random()*5|0]
        };
    });
</script>

{#if $inspected.name}
    <nav>
        <h1>Selected</h1>
        <h2><span>name:</span> {$inspected.name}</h2>
        <h2><span>type:</span> application/vnd.ms-excel</h2>
        <h2><span>Location:</span> /root/projects</h2>
        <h2><span>size on disc:</span> {fakedata.size}</h2>
        <hr>
        <h1>File Permissions</h1>
        <h2><span>Owner:</span> {fakedata.owner}</h2>
        <h2><span>Group:</span> {fakedata.group}</h2>
        <h2><span>Others:</span> Read</h2>
        <hr>
        <h1>Notes</h1>
        <p>{fakedata.notes}</p>
        <hr>
        <h1>File Actions</h1>
        <li>download</li>
        <li>share</li>
        <li>convert</li>
        <li>delete</li>
        <li>rename</li>
    </nav>
{/if}

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
