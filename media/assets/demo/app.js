var Tweet = Backbone.Model.extend({
	defaults: {
		'autor': '', 
		'status': ''
	}
});

var TweetList = Backbone.Collection.extend({
	model : Tweet
});

var twet1 = new Tweet({autor: 'Pepito', status: 'IDIC'});
var twet2 = new Tweet({autor: 'Jorge', status: 'RENIEC'});
var twet3 = new Tweet({autor: 'Hernan', status: 'FABLAB'});

var x = new TweetList([twet1, twet2, twet3]);

console.log(twet1.get('status'));
console.log(x.toJSON());