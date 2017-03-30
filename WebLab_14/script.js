function emailValidate(){
	var x = document.forms.input.username.value;
	var atPos = x.indexOf("@");
	var dotPos = x.lastIndexOf(".");
	
	if (atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length)
		return(false);
	else
		return(true);
}

function passwordValidate(){
	var y = document.forms.input.password.value;
	
	if (y.length < 6)
		return(false);
	else
		return(true);
}

function check() {
	x = emailValidate();
	y = passwordValidate();
	if (x == false)
		if (y == false)
			alert("Both your email and passoword is not valid(password must be at least 6 characters)");
		else 
			if (y == true)
			 alert("Please enter a valid email");
	if (x == true)
		if (y == false)
			alert("Please enter a password with at least 6 characters")
		else 
			if (y == true)
			 alert("Access Granted")
}