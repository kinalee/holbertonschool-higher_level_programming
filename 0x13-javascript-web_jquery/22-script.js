$.get('http://swapi.co/api/films?format=json', function (body) {
  $.each(body.results, function (key, value) {
    $('UL#list_movies').append($('<LI></LI>').text(value.title));
  });
});
