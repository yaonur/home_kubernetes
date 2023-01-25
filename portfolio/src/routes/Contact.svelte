<script>

</script>
<div class="container">
	<h1>Contact Form</h1>
	<form action="https://formsubmit.io/send/686ba150-c09c-46e8-9e5b-8e3ab0d38df0" method="POST">
		<input name="_redirect" type="hidden" id="name" value="http://so2homelab.com/success">
		<input type="text" name="Name" placeholder="Name" required>
		<input type="email" name="email" placeholder="email">
		<input type="text" name="Company" placeholder="Company name">
		<input type="text" name="url" placeholder="Company url">
		<div class="radio-groups">
			<i>Work Type:</i>
			<div class="work-type-input">
				<input type="radio" name="work-type" value="remote" checked> Remote
				<input type="radio" name="work-type" value="on-site"> On-site
				<input type="radio" name="work-type" value="hybrid"> Hybrid
			</div>
		</div>
		<textarea name="Message" id="" cols="30" rows="10"></textarea>
		<button type="submit">Send</button>
	</form>
</div>


<style>
	.container {
		margin: auto;
		width: 80%;
		padding: 1rem;
	}
	
	form {
		display: flex;
		flex-direction: column;
		width: 24rem;
		gap: 1rem;
	}
	
	input, textarea {
		font-size: 20px;
		padding: .6rem;
	}
	
	button {
		padding: 1rem;
		cursor: pointer;
		background: var(--primary-color);
		color: var(--body-color);
		font-size: 24px;
		font-weight: 1000;
		text-decoration: none;
		border: none;
		
	}
	
	button:hover {
		background: var(--hover-primary-color);
	}
	.radio-groups{
		display: flex;
		align-content: center;
		align-items: center;
		color:var(--text-color);
		font-weight: 800;
	}
</style>