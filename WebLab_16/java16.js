function mouse()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	window.addEventListener("mousemove", icon, false);
}

function icon(e) 
{
	canvas.clearRect(0, 0, 600, 600);
	var xpos = e.clientX;
	var ypos = e.clientY;
	
	var pic = new Image();
	pic.src = "http://images.eastbay.com/pi/18765/large/diamond-dol-a-official-league-baseball";
	
	canvas.drawImage(pic, xpos - 100, ypos - 100, 200, 200);
}

window.addEventListener("load", mouse, false);