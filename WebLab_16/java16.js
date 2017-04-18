function mouse()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	window.addEventListener("mousemove", icon, false);
}

function icon(e) 
{
	canvas.clearRect(0, 0, 925, 925);
	var xpos = e.clientX;
	var ypos = e.clientY;
	
	var pic = new Image();
	pic.src = "https://d30y9cdsu7xlg0.cloudfront.net/png/42540-200.png";
	
	canvas.drawImage(pic, xpos - 100, ypos - 100, 200, 200);
}

window.addEventListener("load", mouse, false);