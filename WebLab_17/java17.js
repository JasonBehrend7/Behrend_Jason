function drag() {
	fox = document.getElementById("fox");
	leftBox = document.getElementById("leftBox");
	
	fox.addEventListener("dragstart", startDrag, false);
	fox.addEventListener("dragend", endDrag, false);
	
	leftBox.addEventListener("dragenter", dragEnter, false);
	leftBox.addEventListener("dragleave", dragLeave, false);
	leftBox.addEventListener("dragover", function(e) {e.preventDefault()}, false);
	leftBox.addEventListener("drop", drop, false);
}

function startDrag(e) {
	var pic = '<img id = "fox" src = "https://ichef.bbci.co.uk/news/624/cpsprodpb/F38E/production/_84005326_thinkstockphotos-460190767.jpg">';
	e.dataTransfer.setData('Picture', pic);
}

function dragEnter(e) {
	e.preventDefault();
	leftBox.style.background = "lightBlue";
	leftBox.style.border = "3px solid red";
}

function dragLeave(e) {
	e.preventDefault();
	leftBox.style.background = "white";
	leftBox.style.border = "3px solid blue";
}

function drop(e) {
	e.preventDefault();
	leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e) {
	pic = e.target;
	pic.style.visibility = "hidden";
}

window.addEventListener("load", drag, false);