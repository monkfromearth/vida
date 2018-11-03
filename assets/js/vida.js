function Vida(source, target){
	window.vidaClient = this;
	this.routes = {
	    'api:authorize':'/api/authorize',
	    'api:help#languages':'/api/help/languages',
	    'api:engine#transliterate':'/api/engine/transliterate'
	};
	this.setup = function(){
		NProgress.start();
		$.post(window.vidaClient.routes['api:authorize'], {}, function(ajax){
			if (ajax.status)
				window.csrf_token = ajax.content.csrf_token;
			else {
				console.error("Couldn't authenticate the SDK.");
				return false;
			}
			NProgress.done();
		}).fail(function(e, s, t){
			NProgress.done();
			console.error(e);
			console.error(s);
			console.error(t);
		});
		if ($.inArray(this.source, Object.keys(this.codes)) == -1){
			console.error("Please specify the correct code for the source langauge;");
			return false;
		}
		if ($.inArray(this.target, Object.keys(this.codes)) == -1){
			console.error("Please specify the correct code for the target langauge;");
			return false;
		}
	};
	this.codes = languages = {
		"hin": "Hindi",
		"ben": "Bengali",
		"guj": "Gujarati",
		"pun": "Punjabi",
		"mal": "Malayalam",
		"kan": "Kannada",
		"tam": "Tamil",
		"tel": "Telugu",
		"ori": "Oriya",
		"mar": "Marathi",
		"ass": "Assamese",
		"kon": "Konkani",
		"bod": "Bodo",
		"nep": "Nepali",
		"urd": "Urdu",
		"eng": "English"
	};
	this.source = source;
	this.target = target;
	this.text = null;
	this.config = function(name, value){
		if (name == 'source')
			this.source = value;
		if (name == 'target')
			this.target = value;
	};
	this.setTransliteratedText = function(id, currentProcessId, text){
		if ($(id).attr('vida-ghost-cp-id') == currentProcessId)
			$(id).val(text + " ");
	};
	this.startEngine = function(id){
		this.setup();
		$(id).keypress(function(e){
			if (e.keyCode == 32){
				var text = $(id).val();
				var currentProcessId = Math.random().toString(36).substring(7);
				$(id).attr('vida-ghost-cp-id', currentProcessId);
				$.post(window.vidaClient.routes['api:engine#transliterate'], {
					csrf_token:window.csrf_token,
					source:this.source,
					target:this.target,
					text:text
				}, function(ajax){
					console.log(ajax);
					if (ajax.status)
						window.vidaClient.setTransliteratedText(id, currentProcessId, ajax.content.output);
				}).fail(function(e, s, t){
					console.error(e);
					console.error(s);
					console.error(t);
				});
			};
		});
	};
};