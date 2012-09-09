PageManager = {
	'vote': function(entity_id, entity_type, vote) {
		$.post(
			'/vote',
			{
				entity_id: entity_id,
				entity_type: entity_type,
				vote: vote
			},
			function (data) {
				console.log('eh what?');
				location.reload();
			}
		);
	},
	'register_events': function() {
		$('i.icon-arrow-up, i.icon-arrow-down').click(function() {
			$element = $(this);
			PageManager.vote($element.data('entity-id'), $element.data('entity-type'), $element.data('vote'));
		});
	}
};

$(document).ready(PageManager.register_events);
