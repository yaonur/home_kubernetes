<script>
	import {Router, Link, Route} from "svelte-navigator";
	import Header from "./lib/Header.svelte"
	import Menu from "./lib/Menu.svelte";
	import Home from "./routes/Home.svelte";
	import About from "./routes/About.svelte";
	import Projects from "./routes/Projects.svelte";
	import Contact from "./routes/Contact.svelte";
</script>

<Router>
	<nav>
		<div class="sidebar">
			<Header></Header>
			<Menu></Menu>
		</div>
	
	</nav>
	<div>
		<Route path="/">
			<Home/>
		</Route>
		<Route path="about" component={About}/>
		<Route path="projects" component={Projects}/>
		<Route path="contact" component={Contact}/>
	</div>
</Router>

<style>
	
	.sidebar {
		position: fixed;
		top: 0;
		left: 0;
		height: 100%;
		width: 250px;
		padding: 10px 14px;
		background: var(--sidebar-color)
	}

</style>