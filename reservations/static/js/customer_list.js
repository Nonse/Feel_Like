$('.delete').on('click', function(e) {
	if (!confirm('Are you sure you want to delete the customer?')){
		e.preventDefault();
	}
})
