casper.test.comment('Django-Casper save image test');

// required due to bug in PhantomJS
// http://stackoverflow.com/questions/26608391/using-phantomjs-to-embed-all-images-of-a-webpage-produces-warnings-but-works/26688062#26688062
setTimeout(function(){
    phantom.exit();
}, 0);

var helper = require('./djangocasper.js');

helper.scenario(
    '/', 
    function() {
	this.test.assertSelectorHasText('input',
					'Save as PNG', 
					"The home page has a save button");
	this.click('input[type="submit"]');
    }
);
helper.run();
