// fetches and replaces the name from Star Wars API
$.get('http://swapi.co/api/people/5/?format=json', function (body) {
  $('DIV#character').text(body.name);
});
