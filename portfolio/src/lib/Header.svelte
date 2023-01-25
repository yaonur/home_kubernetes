<script>
	import svelteLogo from '../assets/svelte.svg';
</script>
<header>
	<div class="image-text">
					<span class="image">
						<img src="{svelteLogo}" alt="svLogo">
					</span>
		<div class="text header-text">
			<span class="name">Powered by</span>
			<span class="kind">svelte SPA!!!</span>
		</div>
	</div>
	
</header>

<style>
	header {
		position: relative;
	}
	
	.image-text img {
		width: 40px;
		border-radius: 6px;
	}
	
	header .image-text {
		display: flex;
		align-items: center;
	}
	
	header .image-text .header-text {
		display: flex;
		flex-direction: column;
	}
	
	/*reusables*/
	.text {
		font-size: 16px;
		font-weight: 500;
	}
	
	.image {
		min-width: 60px;
		display: flex;
		align-items: center;
	}
	
	.name {
		font-weight: 800;
	}
	
	.kind {
		/*margin-top: -2px;*/
	}
	
	
	

</style>