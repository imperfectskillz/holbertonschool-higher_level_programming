$.get('https://swapi.co/api/films/?format=json', function (data) {
    let results = data['results'];
    $.each(results, function (error, body) {
	if (error) {
	    console.log(error);
	} else {
#('#list_movies').append('<li>' + body['title'] + '</li>');
	};
    });
}
