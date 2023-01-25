<script>
	import {Router, Link, Route} from "svelte-navigator";
	import {fly} from 'svelte/transition'
	import Header from "./lib/Header.svelte"
	import Menu from "./lib/Menu.svelte";
	import Home from "./routes/Home.svelte";
	import About from "./routes/About.svelte";
	import Projects from "./routes/Projects.svelte";
	import Contact from "./routes/Contact.svelte";
	import Success from "./routes/Success.svelte";
	
	let closed = true
	
	const toggle = () => {
		console.log("pressed")
		closed = !closed
		
	}
</script>

<Router>
	<nav>
		<div class="sidebar" class:closed>
			<div class="arrow-background" class:arrClosed={closed} on:click={toggle}>
				<i class={closed? 'bx bx-chevrons-right':'bx bx-chevrons-left'}></i>
			</div>
			
			{#if !closed}
				<div transition:fly={{x:-100,y:-100,duration:300,delay:0}}>
					<Header></Header>
				</div>
			{/if}
			
			<Menu></Menu>
		</div>
	</nav>
	<div class="page" class:pageClosed={closed}>
		<Route path="/">
			<Home/>
		</Route>
		<Route path="about" component={About}/>
		<Route path="projects" component={Projects}/>
		<Route path="contact" component={Contact}/>
		<Route path="success" component="{Success}"/>
	</div>
</Router>

<style>
	.page {
		transition: var(--tran);
		position: fixed;
		top: 0;
		left: 300px;
		width: 100%;
		height: 100%;
	}
	
	.pageClosed {
		left: 100px;
	}
	
	.sidebar {
		transition: var(--tran);
		position: fixed;
		overflow: hidden;
		top: 0;
		left: 0;
		height: 100%;
		width: 250px;
		padding: 10px 14px;
		background: var(--sidebar-color)
	}
	
	.arrow-background {
		z-index: 10;
		position: absolute;
		top: 3%;
		right: 3px;
		transform: translateY(-50%);
		font-size: 22px;
		padding: 4px;
		background: var(--primary-color);
		opacity: 90%;
		display: flex;
		align-items: center;
		justify-content: center;
		border-radius: 50%;
	}
	
	.arrClosed {
		right: 15px;
	}
	
	.closed {
		width: 35px;
		padding-top: 65px;
	}

</style>