/*! login/index.js 
	variables : mensaje
*/

$( document ).ready(function() {
	var login = $('#login-template').html();
	var template = Handlebars.compile(login);
	var data = {'BASE_URL': BASE_URL, 'mensaje': mensaje};
	var template_compiled = template(data);

	$('body').html(template_compiled);
});