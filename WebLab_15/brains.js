function shapes()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	var g = canvas.createLinearGradient(150, 150, 375, 350);
	g.addColorStop(0, "blue");
	g.addColorStop(0.5, "white");
	g.addColorStop(1, "red");
	
	canvas.strokeStyle = "black";
	canvas.fillStyle = g;
	
	canvas.beginPath();
	canvas.moveTo(300, 50);
	canvas.lineTo(325, 150);
	canvas.lineTo(450, 100);
	canvas.lineTo(375, 200);
	canvas.lineTo(500, 225);
	canvas.lineTo(375, 250);
	canvas.lineTo(450, 350);
	canvas.lineTo(325, 300);
	canvas.lineTo(300, 400);
	canvas.lineTo(275, 300);
	canvas.lineTo(150, 350);
	canvas.lineTo(225, 250);
	canvas.lineTo(100, 225);
	canvas.lineTo(225, 200);
	canvas.lineTo(150, 100);
	canvas.lineTo(275, 150);
	canvas.closePath();
	canvas.fill();
	canvas.stroke();
}

window.addEventListener("load", shapes, false);