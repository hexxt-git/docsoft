<script lang="ts">
	import { writable } from "svelte/store";
	import Inspector from "./Inspector.svelte";


	export let inspected = writable({})

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
	let contextMenu: HTMLElement;
	let selected_nodes: Array<number> = [];

	const click = (e: MouseEvent) => {
		if (e.target == mainElement || e.target == containerElement) {
			selected_nodes = [];
		}
	};

	const mouseDown = (e: MouseEvent) => {
		contextMenu.setAttribute('style', 'display: none');
		if (e.button == 2) {
			let rect = mainElement.getBoundingClientRect();
			let x = mouse.x - rect.x;
			let y = mouse.y - rect.y;
			contextMenu.setAttribute(
				'style',
				`
				top: ${y}px;
				left: ${x}px;
				display: block;
			`,
			);
			return;
		}

		if (e.target == mainElement || e.target == containerElement) {
			mouse.drag = true;
			mouse.move = false;
			selected_nodes = [];
			mainElement.classList.add('drag');
		} else {
			mouse.move = true;
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
		mouse.dx = e.clientX - mouse.x;
		mouse.dy = e.clientY - mouse.y;
		mouse.x = e.clientX;
		mouse.y = e.clientY;

		if (mouse.drag) {
			target_translate.x += mouse.dx;
			target_translate.y += mouse.dy;
		}
		if (mouse.move) {
			physical_fs.forEach((node) => {
				if (selected_nodes.includes(node.id))
					node.move({ x: mouse.dx, y: mouse.dy });
			});
		}
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
			0.4,
		);
		current_translate.y = lerp(
			current_translate.y,
			target_translate.y,
			0.4,
		);
		if (containerElement)
			containerElement.style.transform = `translate(${current_translate.x}px, ${current_translate.y}px)`;
		if (mainElement)
			mainElement.style.backgroundPosition = `${current_translate.x}px ${current_translate.y}px`;

		requestAnimationFrame(container_update);
	};
	if (typeof window != 'undefined') {
		target_translate.x = (window.innerWidth - 400) / 4;
		target_translate.y = window.innerHeight / 2;
		current_translate.x = target_translate.x;
		current_translate.y = target_translate.y;
	}
	container_update();

	class Node {
		image: string;
		name: string;
		id: number;
		creation_date: number;
		modification_date: number;
		children: Array<Node>;

		constructor(
			image: string,
			name: string,
			id: number,
			creation_date: number,
			modification_date: number,
		) {
			this.image = image;
			this.name = name;
			this.id = id;
			this.creation_date = creation_date;
			this.modification_date = modification_date;
			this.children = [];
		}

		async rquest_children() {
			return new Promise((res) =>
				setTimeout(() => {
					this.children = new Array(Math.ceil(Math.random() * 6 + 1))
						.fill(0)
						.map(() => {
							return new Node(
								['folder.svg', 'file.svg'][
									Math.floor(Math.random() * 2)
								],
								[ 'child', 'parent', 'programming', 'art', 'video games', 'movies', 'work', 'horses', 'dogs', 'houses', 'music', 'sports', 'travel', 'education', 'health', 'fitness', 'technology', 'nature', 'science', 'history','photography', 'cooking', 'literature', 'design', 'fashion', 'business', 'finance', 'politics', 'culture', 'architecture', 'gardening', 'crafts', 'automobiles', 'real estate', 'shopping', 'entertainment', 'news', 'religion', 'philosophy', 'psychology','sociology', 'economics', 'mathematics', 'physics', 'chemistry', 'biology', 'astronomy', 'geography', 'languages', 'coding','web development', 'software engineering', 'data science', 'machine learning', 'artificial intelligence', 'networking', 'cybersecurity','databases', 'cloud computing', 'virtual reality', 'augmented reality', 'blockchain', 'cryptocurrency', 'robotics', 'quantum computing','sustainability', 'environment', 'climate change', 'renewable energy', 'conservation', 'wildlife', 'outdoors', 'camping', 'hiking','yoga', 'meditation', 'mindfulness', 'nutrition', 'weight loss', 'bodybuilding', 'running', 'cycling', 'swimming', 'basketball','soccer', 'baseball', 'football', 'tennis', 'golf', 'skiing', 'surfing', 'rock climbing', 'fishing', 'painting', 'drawing', 'sculpture','pottery', 'photography', 'filmmaking', 'animation', 'graphic design', 'interior design', 'landscape design', 'fashion design', 'jewelry design','knitting', 'sewing', 'quilting', 'scrapbooking', 'woodworking', 'metalworking', 'calligraphy', 'origami', 'magic', 'juggling', 'stand-up comedy'][Math.random()*100|0],
								Math.trunc(Math.random() * 100000),
								0,
								0,
							);
						});
					res(1);
					//console.log(...this.children);
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
			setTimeout(() => res(new Node('folder.svg', 'root', 0, 0, 0)), 500),
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
		htmlElement: HTMLElement | undefined;
		is_open: boolean;
		direction: number;
		depth: number;
		parent: PhysicalNode | undefined;
		image: string;
		is_connected: boolean = true;
		constructor(
			name: string,
			direction: number,
			position: Vector2,
			id: number,
			depth: number,
			parent: PhysicalNode | undefined,
			image: string,
		) {
			this.name = name;
			this.base_position = { x: position.x, y: position.y };
			this.id = id;
			this.wobble_dir = Math.random() * Math.PI * 2;
			this.velocity = { x: 0, y: 0 };
			this.is_open = false;
			this.direction = direction;
			this.position = {
				x: position.x + Math.random() * 50 - 25,
				y: position.y + Math.random() * 50 - 25,
			};
			//this.position = position;
			this.depth = depth;
			this.parent = parent;
			this.image = image;
		}
		update() {
			let wobble_speed = 0.02;
			let tedancy_to_base = 0.001;

			this.position.x += this.velocity.x;
			this.position.y += this.velocity.y;
			this.velocity.x += Math.cos(this.wobble_dir) * wobble_speed;
			this.velocity.y += Math.sin(this.wobble_dir) * wobble_speed;

			this.velocity.x *= 0.9;
			this.velocity.y *= 0.9;
			if (typeof this.htmlElement !== 'undefined') {
				this.htmlElement.setAttribute(
					'style',
					`top: ${this.position.y}px; left: ${this.position.x}px; scale: ${zoom_level};`,
				);
			}

			let randomization = 0.3;
			this.wobble_dir +=
				Math.random() * randomization - randomization / 2;

			let dx = this.base_position.x - this.position.x;
			let dy = this.base_position.y - this.position.y;
			this.velocity.x += dx * tedancy_to_base;
			this.velocity.y += dy * tedancy_to_base;

			if (
				Math.abs(this.position.x - this.base_position.x) > 500 ||
				Math.abs(this.position.y - this.base_position.y) > 500
			) {
				this.position = this.base_position;
				this.velocity = { x: 0, y: 0 };
			}

			if (typeof this.parent != 'undefined')
				this.direction =
					180 +
					(Math.atan2(
						this.parent.position.y - this.position.y,
						this.parent.position.x - this.position.x,
					) * 180) / Math.PI;
		}
		mouseDown(e: MouseEvent) {
			if (e.shiftKey) {
				if (selected_nodes.includes(this.id)) {
					selected_nodes = selected_nodes.filter(
						(id) => id != this.id,
					);
				} else {
					selected_nodes = [...selected_nodes, this.id];
				}
			} else if (!selected_nodes.includes(this.id)) {
				selected_nodes = [this.id];
			}
		}
		async open() {
			if(this.image == 'file.svg') return 0;
			const node: Node | 0 = fs.findChild(this.id);
			if (typeof node == 'number') return 0;
			selected_nodes = [this.id];
			this.is_open = true;
			await node.rquest_children();
			
			if(typeof window != 'undefined'){
				target_translate.x = - this.position.x + (window.innerWidth - 400)/2
				target_translate.y = - this.position.y + window.innerHeight/2
			}
			
			const physical_chilren: Array<PhysicalNode> = node.children.map(
				(child, index) => {
					// evenly distrebute from the current direction in a 30deg
					let area = 90;
					if(this.depth == 1) area = 360;
					let spread = area / node.children.length;
					let child_direction =
						this.direction + spread * (index + 0.5) - area / 2;
					if (node.children.length == 1)
						child_direction = this.direction;
					const child_position = {
						x:
							this.position.x +
							Math.cos((child_direction * Math.PI) / 180) *
								((this.depth + 3) * 2) ** 0.7 *
								80,
						y:
							this.position.y +
							Math.sin((child_direction * Math.PI) / 180) *
								((this.depth + 3) * 2) ** 0.7 *
								80,
					};
					return new PhysicalNode(
						child.name,
						child_direction,
						child_position,
						child.id,
						this.depth + 1,
						this,
						child.image,
					);
				},
			);

			physical_chilren.forEach((child) => {
				links = [
					...links,
					{ p1: this, p2: child, htmlElement: undefined },
				];
			});

			physical_fs = [...physical_fs, ...physical_chilren];
		}
		close() {
			const node: Node | 0 = fs.findChild(this.id);
			if (typeof node == 'number') return 0;
			selected_nodes = [];
			const close_recursive = (node: Node) => {
				node.children.forEach((child) => {
					const physical_node = physical_fs.find(
						(physical_node) => physical_node.id == child.id,
					);
					if (typeof physical_node !== 'undefined') {
						close_recursive(child);
						physical_fs = physical_fs.filter(
							(physical_node) => physical_node.id != child.id,
						);
						links = links.filter(
							(link) =>
								link.p1.id != child.id &&
								link.p2.id != child.id,
						);
					}
				});
			};

			// ... rest of the code
			close_recursive(node);
			this.is_open = false;
		}
		doubleClick() {
			if (!this.is_open) this.open();
			else this.close();
			if(this.image == 'file.svg') window.open('/file_viewer/'+this.id)
		}
		move(distance: Vector2) {
			this.base_position.x += distance.x;
			this.base_position.y += distance.y;
			this.position.x = this.base_position.x;
			this.position.y = this.base_position.y;

			if (this.id == 0) return;
			const node: Node | 0 = fs.findChild(this.id);
			if (typeof node == 'number') return 0;
			node.children.forEach((child) => {
				const physical_node = physical_fs.find(
					(physical_node) => physical_node.id == child.id,
				);
				if (typeof physical_node !== 'undefined') {
					physical_node.move(distance);
				}
			});
		}
		moveTo(position: Vector2) {
			const distance = {
				x: position.x - this.position.x,
				y: position.y - this.position.y,
			};
			this.move(distance);
		}
		async rename(new_name: string) {
			return new Promise((res) =>
				setTimeout(() => {
					this.name = new_name;
					// api call
					res(1);
				}, 500),
			);
		}
		async delete() {
			return new Promise((res) =>
				setTimeout(() => {
					this.close();
					physical_fs = physical_fs.filter(
						(physical_node) => physical_node.id != this.id,
					);
					links = links.filter(
						(link) =>
							link.p1.id != this.id && link.p2.id != this.id,
					);
					// api call
					res(1);
				}, 500),
			);
		}
	}

	interface Link {
		p1: PhysicalNode;
		p2: PhysicalNode;
		htmlElement: SVGLineElement | undefined;
	}

	let physical_fs: Array<PhysicalNode> = [];
	let links: Array<Link> = [];

	const init_physical_fs = async () => {
		physical_fs = [
			...physical_fs,
			new PhysicalNode(
				fs.name,
				0,
				{ x: 0, y: 0 },
				fs.id,
				1,
				undefined,
				fs.image,
			),
		];
	};

	const init = async () => {
		await init_fs();
		await init_physical_fs();
		physical_fs[0].open();
	};

	let push_force = 0.05;
	const physics_update = () => {
		if (typeof window == 'undefined') return;
		physical_fs.forEach((node) => {
			node.update();
		});

		physical_fs.forEach((node1) => {
			// this O(n^2) algorithm should be optimized later
			physical_fs.forEach((node2) => {
				if (node1 == node2) return;

				const dx = node2.position.x - node1.position.x;
				const dy = node2.position.y - node1.position.y;
				const distance = Math.sqrt(dx * dx + dy * dy);
				const minDistance = 120;

				if (distance < minDistance) {
					const angle = Math.atan2(dy, dx);
					const targetX =
						node1.position.x + Math.cos(angle) * minDistance;
					const targetY =
						node1.position.y + Math.sin(angle) * minDistance;

					const ax = (targetX - node2.position.x) * push_force;
					const ay = (targetY - node2.position.y) * push_force;

					node1.position.x -= ax;
					node1.base_position.x -= ax;
					node1.position.y -= ay;
					node1.base_position.y -= ay;
					node2.position.x += ax;
					node2.base_position.x += ax;
					node2.position.y += ay;
					node2.base_position.y += ay;
				}
			});
		});

		inspected.set(fs?.findChild(selected_nodes[selected_nodes.length-1]) || {})
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

		ctx.strokeStyle = '#202432';
		ctx.fillStyle = 'white';
		ctx.lineWidth = 5;

		ctx.clearRect(0, 0, linkCanvas.width, linkCanvas.height);

		// add current_translateZ
		links.forEach((link) => {
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
			ctx.fillRect(
				link.p1.base_position.x + current_translate.x - 4,
				link.p1.base_position.y + current_translate.y - 4,
				8,
				8,
			);
			ctx.fillRect(
				link.p2.base_position.x + current_translate.x - 4,
				link.p2.base_position.y + current_translate.y - 4,
				8,
				8,
			);
		});

		requestAnimationFrame(draw_links);
	};

	draw_links();

	init();
</script>

<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
<!-- svelte-ignore a11y-click-events-have-key-events -->
<main
	on:mousedown={mouseDown}
	on:mouseup={mouseUp}
	bind:this={mainElement}
	on:wheel={wheelMove}
	on:contextmenu|preventDefault
	on:click={click}
	class="main"
>
	<canvas bind:this={linkCanvas}></canvas>
	<div id="container" bind:this={containerElement}>
		{#each physical_fs as node}
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<!-- svelte-ignore a11y-no-static-element-interactions -->
			<div
				class="node {selected_nodes.includes(node.id)
					? 'selected'
					: ''}"
				on:mousedown={(e) => node.mouseDown(e)}
				on:dblclick={() => node.doubleClick()}
				bind:this={node.htmlElement}
				style="translate({node.position.x}px, {node.position.y}px);"
			>
				<img draggable="false" src={node.image} alt="" />
				<div class="node-name">
					{node.image=='file.svg'?'':'/'}{node.name}</div>
				{#if selected_nodes.includes(node.id)}
					<div class="highlight"></div>
				{/if}
			</div>
		{/each}
	</div>
	<div id="context-menu" bind:this={contextMenu}>
		<div class="menu-item">
			copy
			<span>ctrl + c</span>
			<hr>
		</div>
		<div class="menu-item">
			paste
			<span>ctrl + v</span>
			<hr>
		</div>
		<div class="menu-item">
			cut
			<span>ctrl + x</span>
			<hr>
		</div>
		<div class="menu-item">
			rename
			<span>ctrl + f2</span>
			<hr>
		</div>
		<div class="menu-item">
			preview
			<span>ctrl + o</span>
			<hr>
		</div>
		<div class="menu-item">
			download
			<span>ctrl + s</span>
			<hr>
		</div>
		<div class="menu-item">
			share
			<span>ctrl + a</span>
			<hr>
		</div>
		<div class="menu-item">
			convert
			<span>ctrl + t</span>
		</div>
	</div>
</main>

<style>
	main {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background-color: white;
		background-image: radial-gradient(#f0f0f0 4px, transparent 5px);
		background-position: 0 0;
		background-size: 45px 45px;
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
		width: 80px;
		height: 80px;
		border-radius: 100%;
		background: var(--node-color);
		box-shadow:
			var(--node-shadow) -7px 5px 10px -3px,
			var(--node-shadow) 6px -6px 12px -6px;
		color: white;
		display: flex;
		justify-content: center;
		align-items: center;
		transform: translate(-50%, -50%) scale(100%);
		cursor: pointer;
		user-select: none;
		text-align: center;
		transition: transform 200ms ease-in;
	}
	.node:hover,
	.node:global(.selected) {
		transform: translate(-50%, -50%) scale(115%);
	}
	.node .highlight {
		border: solid var(--accent) 2px;
		position: absolute;
		top: -2px;
		left: -2px;
		width: 100%;
		height: 100%;
		border-radius: 100%;
		box-shadow: var(--accent) 0 0 10px;
	}
	.node img {
		width: 40px;
		height: 40px;
		z-index: 15;
	}
	.node-name {
		position: absolute;
		top: 70%;
		left: 50%;
		background-color: var(--node-color);
		z-index: 10;
		padding: 5px 15px;
		border-radius: 8px;
		width: max-content;
		max-width: 120px;
		box-shadow: var(--node-color) -2px 1px 10px;
	}
	canvas {
		position: absolute;
		top: 0;
		left: 0;
		pointer-events: none;
		filter: blur(1px);
	}
	#context-menu {
		background-color: #fff;
		color: black;
		position: absolute;
		top: 0;
		left: 0;
		display: none;
		border-radius: 30px;
		padding: 10px 0;
		overflow: hidden;
	}
	#context-menu .menu-item {
		padding: 10px;
		width: 210px;
		cursor: pointer;
	}
	#context-menu .menu-item:hover {
		padding-left: 20px;
		padding-right: 0;
		text-decoration: underline;
	}
	.menu-item:nth-child(odd) {
		background-color: #fff;
	}
	.menu-item:nth-child(even) {
		background-color: #fafafa;
	}
	hr{
		border-style: solid;
		border-color: #888;
		border-width: 1px;
		width: 70%;
		position: absolute;
		bottom: 0;		
		left: 0;
		right: 0;
		transform: translateY(11px);
	}
	.menu-item{
		display: flex;
		justify-content: space-between;
		position: relative;
	}
	.menu-item span{
		text-decoration: none;
		position: absolute;
		right: 10px;
		color: #888;
		text-transform: uppercase;
	}
</style>
