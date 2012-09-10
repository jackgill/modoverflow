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
				location.reload();
			}
		);
	},
	'accept': function(answer_id, question_id) {
		$.post(
			'/answers/accept',
			{
				answer_id: answer_id,
				question_id: question_id
			},
			function (data) {
				location.reload();
			}
		);
	},
	'register_events': function() {
		// Voting
		$('i.icon-arrow-up, i.icon-arrow-down').click(function() {
			$element = $(this);
			PageManager.vote($element.data('entity-id'), $element.data('entity-type'), $element.data('vote'));
		});

		// Accept answer
		$('button.accept-answer').click(function() {
			$element = $(this);
			PageManager.accept($element.data('answer-id'), $element.data('question-id'));
		});
	}
};

$(document).ready(PageManager.register_events);
