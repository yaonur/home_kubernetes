<script>
	import {link} from "svelte-navigator";
</script>
<div  >
	<div >
		<ul >
			<li >
				<a href="/" use:link>
					<i class='bx bx-home-alt'></i>
					<span>Home</span>
				</a>
			</li>
			<li >
				<a href="about" use:link>
					<i class='bx bx-user'></i>
					<span>About</span>
				</a>
			</li>
			<li >
				<a href="projects" use:link>
					<i class='bx bx-briefcase'></i>
					<span>Projects</span>
				</a>
			</li>
			<li >
				<a href="contact" use:link>
					<i class='bx bx-user-pin'></i>
					<span>Contact</span>
				</a>
			</li>
		</ul>
	</div>
</div>


<style>
	ul {
		margin: 0;
		padding: 0;
	}
	
	li {
		height: 50px;
		/*background: red;*/
		margin-top: 10px;
		list-style: None;
		display: flex;
		align-items: center;
	}
	
	a {
		height: 100%;
		width: 100%;
		display: flex;
		align-items: center;
		/*justify-content: space-around;*/
		text-decoration: none;
		border-radius: 6px;
		transition: var(--tran);
	}
	
	a:hover {
		background: var(--primary-color);
		
	}
	
	a:hover span, a:hover i {
		color: var(--sidebar-color)
		
		
	}
	
	i {
		margin-left: 8px;
	}
	span{
		margin-left: 25px;
	}
	
	
	span, i {
		font-size: 25px;
		font-weight: 700;
		color: var(--text-color);
		transition: var(--tran);
	}


</style>