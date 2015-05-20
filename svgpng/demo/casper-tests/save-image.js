casper.test.comment('Django-Casper save image test');

// required due to bug in PhantomJS
// http://stackoverflow.com/questions/26608391/using-phantomjs-to-embed-all-images-of-a-webpage-produces-warnings-but-works/26688062#26688062
// setTimeout(function(){
//     phantom.exit();
// }, 0);

var helper = require('./djangocasper.js');

helper.scenario(
    '/', 
    function() {
	// The app has a single form.  Inside this form are two input widgets:
	// * a hidden widget named "csrfmiddlewaretoken"
	// * a submit widget named "Save as PNG"
	// We test the presence of the first.
	// We then try to retrieve the second.
	// Our goal with the second is to submit it as a param in a POST request.
	// The template for the POST request is in base64encode.
	this.test.assertSelectorHasText('input[type="submit"]',
					'Save as PNG', 
					"The home page has a save button");
	this.click('input[type="submit"]');
    }
);
helper.run();
