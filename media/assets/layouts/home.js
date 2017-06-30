/*! layouts/home.js 
	variables : MODULOS_JSON
*/

$( document ).ready(function() {
	var menu_modulos = $('#menu-modulos').html();
	var template = Handlebars.compile(menu_modulos);
	var data = {'base_url': 'HOLA MUNDO!!!'};
	var template_compiled = template(data);

	$('.navbar-nav').html(template_compiled);
});

Handlebars.registerHelper( "menuModulos", function (){
	var rpta = '';
	MODULOS_JSON.forEach(function(modulo) {
	    rpta = rpta + '<li class="dropdown"><a href="' + BASE_URL + modulo['url'] + '" class="dropdown-toggle" data-toggle="dropdown">' + modulo['nombre'] + '</a></li>';
	});
	return rpta;    
});
