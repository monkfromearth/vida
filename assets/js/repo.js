$("[data-toggle=tooltip]").tooltip();

$(function() {
    $('a.onpage-link').click(function(e) {
    	e.preventDefault();
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top-50
        }, 1000);
    });
});

var readImage = function(input, $this) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function(e) {
      $this.attr('src', e.target.result);
    }
    reader.readAsDataURL(input.files[0]);
  }
}

var Codes = {
    'Request':{
        'INPUT_TOO_LONG': "Input too long. Please provide an input of %s or less characters.",
        'EMPTY_INPUT': "Please provide some input to proceed.",
        'INCORRECT_INPUT': "Please provide some valid input.",
        'INCORRECT_CSRF_TOKEN': "Please clear cookies and cache, then try again.",
        'INVALID_CHAR': "Please use valid characters for the input.",
        'INVALID_INPUT': "Please provide some valid input.",
        'INVALID_CAPTCHA': "Please properly fill the reCaptcha.",
        'NO_CONNECTION': "Internet not connected.",
        'INVALID_EMAIL': "Please provide a valid email address."
    },
    'User': {
        'NOT_FOUND': "User not found.",
        'ALREADY_EXISTS': "User with the email already exists.",
        'USERNAME_EXISTS': "Username taken. Please choose another one.",
        'PASSWD_TOO_SHORT': "Please choose a strong password of 8 or more characters.",
        'CONFIRM_PASSWD': "Please confirm the password you entered."
    }
}

var Validator = {
    email: function(email){
      var re = /^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
      return re.test(email);
    }
}

var Repo = {
    notify: function($parent, message, category, $target){
      category = typeof category == 'undefined' ? 'danger' : category;
      $parent.children('.alert').remove();
      $parent.append('<div class="fade alert alert-' + category + '">' + message + '</div>');
      if (typeof $target != 'undefined')
        $target.parent().addClass('has-' + category);
      setTimeout(function(){
        $parent.find('.alert').addClass('in');
      }, 50);
    }
}