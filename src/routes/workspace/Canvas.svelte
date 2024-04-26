<script lang="ts">
	const lerp = (a: number, b: number, t: number) => {
		t = Math.max(0, Math.min(1, t));
		return a + (b - a) * (t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t);
	};

	const mouse = {
		x: 0,
		y: 0,
        dx: 0,
        dy: 0,
		drag: false,
        move: false,
	};
	let mainElement: HTMLElement;
	let containerElement: HTMLElement;
	let current_translate: Vector2 = { x: 0, y: 0 };
	let target_translate: Vector2 = { x: 0, y: 0 };
    let zoom_level = 1; // dont use this
	const mouseDown = (e: MouseEvent) => {
		if(e.target == mainElement || e.target == linkCanvas){
            mouse.drag = true;
            mouse.move = false;
            selected_nodes = []
        }
        else {
            mouse.move = true;
            mainElement.classList.add('drag');
        }
	};
	const mouseUp = () => {
		mouse.drag = false;
        mouse.move = false;
		if (typeof mainElement == 'undefined') return;
		if (mainElement == null) return;
		if (!mainElement.classList.contains('drag')) return;
		
        mainElement.classList.remove('drag');
	};
	if (typeof window != 'undefined') {
		window.addEventListener('mouseup', mouseUp);
	}
	const mouseMove = (e: MouseEvent) => {
		let dragSpeed = 1.2;

		let x = e.clientX * dragSpeed;
		let y = e.clientY * dragSpeed;

        let deltaX = x - mouse.x;
        let deltaY = y - mouse.y;
		
        if (mouse.drag) {
			target_translate.x += deltaX;
			target_translate.y += deltaY;
		}
        if (mouse.move){
            physical_fs.forEach(node => {   
                if(selected_nodes.includes(node.id)) node.move({x: deltaX, y: deltaY});
            });
        }

		mouse.dx = x - mouse.x;
        mouse.dy = y - mouse.y;
        mouse.x = x;
        mouse.y = y;
	};
	if (typeof window != 'undefined') {
		window.addEventListener('mousemove', mouseMove);
	}
	const wheelMove = (e: WheelEvent) => {
		let scrollSpeed = 0.8;
		target_translate.x -= e.deltaX * scrollSpeed;
		target_translate.y -= e.deltaY * scrollSpeed;
	};

	const container_update = () => {
		if (typeof window == 'undefined') return;
		current_translate.x = lerp(
			current_translate.x,
			target_translate.x,
			0.2,
		);
		current_translate.y = lerp(
			current_translate.y,
			target_translate.y,
			0.2,
		);
		if (containerElement)
			containerElement.style.transform = `translate(${current_translate.x}px, ${current_translate.y}px)`;

		requestAnimationFrame(container_update);
	};
	if (typeof window != 'undefined') {
		target_translate.x = (window.innerWidth - 400) / 4;
		target_translate.y = window.innerHeight / 2;
        current_translate = target_translate;
	}
	container_update();

	class Node {
		icon: string;
		name: string;
		id: number;
		creation_date: number;
		modification_date: number;
		children: Array<Node>;

		constructor(
			icon: string,
			name: string,
			id: number,
			creation_date: number,
			modification_date: number,
		) {
			this.icon = icon;
			this.name = name;
			this.id = id;
			this.creation_date = creation_date;
			this.modification_date = modification_date;
			this.children = [];
		}

		async rquest_children() {
			return new Promise((res) =>
				setTimeout(() => {
					this.children = new Array(Math.ceil(Math.random()*5)).fill(0).map(()=>{
                        return new Node(
							'icon.png',
							'child',
							Math.trunc(Math.random() * 100000),
							0,
							0,
						)
                    })
					res(1);
				}, 500),
			);
		}

		findChild(id: number): Node | 0 {
			if (this.id === id) return this;
			for (let child of this.children) {
				let returned = child.findChild(id);
				if (returned != 0) return returned;
			}
			return 0;
		}
	}

	const get_root = async (): Promise<Node> => {
		return new Promise((res) =>
			setTimeout(() => res(new Node('icon.png', 'root', 0, 0, 0)), 500),
		);
	};

	let fs: Node;
	const init_fs = async () => {
		fs = await get_root();
	};

	interface Vector2 {
		x: number;
		y: number;
	}

	class PhysicalNode {
		name: string;
		position: Vector2;
        base_position: Vector2;
		wobble_dir: number;
		velocity: Vector2;
		id: number;
        htmlElement: HTMLElement|undefined;
        is_open: boolean;
        direction: number;
        depth: number;
        parent_id: number;
		constructor(name: string, direction: number, position: Vector2, id: number, depth: number, parent_id: number) {
			this.name = name;
            this.base_position = position;
			this.id = id;
			this.wobble_dir = Math.random()*Math.PI;
			this.velocity = { x: 0, y: 0 };
            this.is_open = false;
            this.direction = direction;
            //this.position = { x: position.x + Math.random()*50 - 25, y: position.y + Math.random()*50 - 25};
			this.position = position;
            this.depth = depth;
            this.parent_id = parent_id;
		}
        update() {
            let wobble_speed = 0.12;
            let attraction_strength = 0.01;

            this.position.x += this.velocity.x;
            this.position.y += this.velocity.y;
            this.position.x += Math.cos(this.wobble_dir) * wobble_speed;
            this.position.y += Math.sin(this.wobble_dir) * wobble_speed;

            if (typeof this.htmlElement !== 'undefined') {
                this.htmlElement.setAttribute('style', `top: ${this.position.y}px; left: ${this.position.x}px; scale: ${zoom_level};`);
            }

            let randomization = 0.5;
            this.wobble_dir += Math.random() * randomization - randomization / 2;

            let dx = this.base_position.x - this.position.x;
            let dy = this.base_position.y - this.position.y;
            this.velocity.x += dx * attraction_strength;
            this.velocity.y += dy * attraction_strength;

            this.velocity.x *= 0.9
            this.velocity.y *= 0.9
        }
		mouseDown(e: MouseEvent) {
			if(e.shiftKey){
                if(selected_nodes.includes(this.id)){
                    selected_nodes = selected_nodes.filter(id => id != this.id);
                }else{
                    selected_nodes = [...selected_nodes, this.id];
                }
            } else {
                selected_nodes = [this.id];
            }
		}
        async open(){
            const node: Node | 0 = fs.findChild(this.id);
			if (typeof node == 'number') return 0;
			selected_nodes = [];
            this.is_open = true;

			await node.rquest_children();
			const physical_chilren: Array<PhysicalNode> = node.children.map(
				(child, index) => {
                    // evenly distrebute from the current direction in a 30deg
                    let area = 60
                    let spread = area / node.children.length
                    let child_direction = this.direction + spread * (index + 0.5) - area/2
                    if(node.children.length == 1) child_direction = this.direction
					const child_position = {
						x: this.position.x + Math.cos(child_direction * Math.PI / 180) * ((this.depth+2) * 2)**0.7 * 80,
						y: this.position.y + Math.sin(child_direction * Math.PI / 180) * ((this.depth+2) * 2)**0.7 * 80,
					};
                    console.log(this.direction, child_direction, index)
					return new PhysicalNode(
						child.name,
                        child_direction,
						child_position,
						child.id,
                        this.depth + 1,
                        this.id,
					);
				},
			);
            
            physical_chilren.forEach(child => {
                links = [...links, {p1: this, p2: child, htmlElement: undefined}];
            });

			physical_fs = [...physical_fs, ...physical_chilren];
			console.log(node, physical_chilren);
        }
        close(){
            const node: Node | 0 = fs.findChild(this.id);
            if (typeof node == 'number') return 0;
            selected_nodes = []
            const close_recursive = (node: Node) => {
                node.children.forEach(child => {
                    const physical_node = physical_fs.find(physical_node => physical_node.id == child.id);
                    if (typeof physical_node !== 'undefined') {
                        close_recursive(child);
                        physical_fs = physical_fs.filter(physical_node => physical_node.id != child.id);
                        links = links.filter(link => link.p1.id != child.id && link.p2.id != child.id);
                    }
                });
            }

            // ... rest of the code
            close_recursive(node);
            this.is_open = false;
        }
		doubleClick() {
			if(!this.is_open) this.open()
            else this.close()
		}
        move(distance: Vector2){
            this.position.x += distance.x;
            this.position.y += distance.y;

            const node: Node | 0 = fs.findChild(this.id);
            if (typeof node == 'number') return 0;
            node.children.forEach(child => {
                const physical_node = physical_fs.find(physical_node => physical_node.id == child.id);
                if (typeof physical_node !== 'undefined') {
                    physical_node.move(distance);
                }
            });
        }
        moveTo(position: Vector2){
            const distance = {x: position.x - this.position.x, y: position.y - this.position.y};
            this.move(distance);
        }
	}

    interface Link{
        p1: PhysicalNode;
        p2: PhysicalNode;
        htmlElement: SVGLineElement|undefined;
    }

	let physical_fs: Array<PhysicalNode> = [];
    let links: Array<Link> = [];
    let selected_nodes: Array<number> = [];

	const init_physical_fs = async () => {
		physical_fs = [
			...physical_fs,
			new PhysicalNode(fs.name, 0, { x: 0, y: 0 }, fs.id, 1),
		];
	};

	const init = async () => {
		await init_fs();
		await init_physical_fs();
		console.log('intialized: ', fs, physical_fs);
	};


    let push_force = 0.5
	const physics_update = () => {
		if (typeof window == 'undefined') return;
		physical_fs.forEach((node) => {
			node.update();
		});

        physical_fs.forEach(node1 => { // this O(n^2) algorithm should be optimized later
            physical_fs.forEach(node2 => {
                if(node1 == node2) return;

                const dx = node2.position.x - node1.position.x;
                const dy = node2.position.y - node1.position.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                const minDistance = 150;

                if (distance < minDistance) {
                    const angle = Math.atan2(dy, dx);
                    const targetX = node1.position.x + Math.cos(angle) * minDistance;
                    const targetY = node1.position.y + Math.sin(angle) * minDistance;

                    const ax = (targetX - node2.position.x) * push_force;
                    const ay = (targetY - node2.position.y) * push_force;

                    node1.position.x -= ax;
                    node1.position.y -= ay;
                    node2.position.x += ax;
                    node2.position.y += ay;
                }
            })
        })

		requestAnimationFrame(physics_update);
	};

	physics_update();

    let linkCanvas: HTMLCanvasElement;
    const draw_links = () => {
        if (typeof window == 'undefined') return;
        if (typeof linkCanvas == 'undefined' || linkCanvas == null) {
            requestAnimationFrame(draw_links);
            return;
        }
        let rect = containerElement.getBoundingClientRect();
        linkCanvas.width = rect.width;
        linkCanvas.height = rect.height;

        const ctx = linkCanvas.getContext('2d');
        if (ctx == null) return;

        ctx.strokeStyle = 'white';
        ctx.lineWidth = 2;

        ctx.clearRect(0, 0, linkCanvas.width, linkCanvas.height);

        // add current_translate
        links.forEach(link => {
            ctx.beginPath();
            ctx.moveTo(
                link.p1.position.x + current_translate.x,
                link.p1.position.y + current_translate.y,
            );
            ctx.lineTo(
                link.p2.position.x + current_translate.x,
                link.p2.position.y + current_translate.y,
            );
            ctx.stroke();
        });
        
        requestAnimationFrame(draw_links);
    }

    draw_links();

	init();
</script>

<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
<main
	on:mousedown={mouseDown}
	on:mouseup={mouseUp}
	bind:this={mainElement}
	on:wheel={wheelMove}
	class="main"
>
    <canvas bind:this={linkCanvas}></canvas>
	<div id="container" bind:this={containerElement}>
		{#each physical_fs as node}
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<!-- svelte-ignore a11y-no-static-element-interactions -->
			<div
				class="node {selected_nodes.includes(node.id) ? 'selected' : ''}"
				on:mousedown={(e) => node.mouseDown(e)}
				on:dblclick={() => node.doubleClick()}
                bind:this={node.htmlElement}
                style="translate({node.position.x}px, {node.position.y}px);"
			>
				{node.name}<br/>{node.id}
			</div>
		{/each}
	</div>
</main>

<style>
    main {
        position: relative;
        background: repeating-linear-gradient(
            45deg,
            transparent,
            transparent 10px,
            rgba(255, 255, 255, 0.05) 10px,
            rgba(255, 255, 255, 0.05) 20px
        );
        overflow: hidden;
    }
	main:global(.drag) {
		cursor: grabbing;
	}
	#container {
		height: 100%;
		overflow: visible;
	}
	.node {
		position: absolute;
		padding: 20px;
        font-size: 15px;
		border-radius: 100%;
		background: #222;
		display: flex;
		justify-content: center;
		align-items: center;
		transform: translate(-50%, -50%) scale(100%);
		cursor: pointer;
		user-select: none;
		text-align: center;
        transition: transform 200ms ease-in-out;
	}
	.node:hover {
		transform: translate(-50%, -50%) scale(110%);
	}
	.node:global(.selected) {
		outline: 2px solid blue;
		outline-offset: 2px;
	}
    canvas{
        position: absolute;
        top: 0;
        left: 0;
    }
</style>
