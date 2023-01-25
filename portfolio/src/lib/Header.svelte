<script>
	import svelteLogo from '../assets/svelte.svg';
	import rightArrow from '../assets/right-arrow-regular-24.png'
</script>
<header>
	<div class="image-text">
					<span class="image">
						<img src="{svelteLogo}" alt="svLogo">
					</span>
		<div class="text header-text">
			<span class="name">Svelte</span>
			<span class="kind">SPA app</span>
		</div>
	</div>
	<div class="arrow-background">
		<i class='bx bx-chevrons-right' ></i>
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
		margin-top: -2px;
	}
	
	
	 i {
		position: absolute;
		top: 50%;
		right: -25px;
		transform: translateY(-50%);
		 font-size: 22px;
		/*height: 20px;*/
		/*width: 20px;*/
		 padding: 4px;
		background: var(--primary-color);
		 opacity: 90%;
		display: flex;
		align-items: center;
		justify-content: center;
		border-radius: 50%;
	}

</style>