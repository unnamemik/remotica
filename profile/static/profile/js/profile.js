const blockes = document.querySelectorAll('.profile_block'),
    boxes = document.querySelectorAll('.profile_box');
let dragElem = null;
blockes.forEach(profile_block =>{
  profile_block.draggable = true;
  profile_block.addEventListener('dragstart', startDragBlock);
  profile_block.addEventListener('dragend', endDragBlock);
});

function startDragBlock(){
  console.log('dragstart');
  dragElem = this;
  setTimeout (()=> {
    this.classList.add('hide');
  }, 0);
}
function endDragBlock(){
  console.log('dragend');
  dragElem = null;
  this.classList.remove('hide');
}

boxes.forEach(profile_box => {
  profile_box.addEventListener('dragover', dragBoxOver);
  profile_box.addEventListener('dragenter', dragBoxEnter);
  profile_box.addEventListener('dragleave', dragBoxLeave);
  profile_box.addEventListener('drop', dropInBox);
})

function dragBoxOver(evt){
  console.log('dragover');
  evt.preventDefault();
  this.classList.add('hover');
}
function dragBoxEnter(evt){
  console.log('dragenter');
  evt.preventDefault();
  this.classList.add('hover');
}
function dragBoxLeave(){
   console.log('dragleave');
  this.classList.remove('hover');
}
function dropInBox(evt){
  console.log('drop');
  this.append(dragElem);
  this.classList.remove('hover');
}

function btn_name (btnId) {
    let but_command=prompt('Введите команду для кнопки: ');
    const button = document.getElementById(btnId);
    button.textContent = but_command;
}


// -----------------------wheel---------------------------

(function(){
	var init, rotate, start, stop, active = false,
	angle = 0,
	rotation = 0,
	startAngle = 0,
	center = {x: 0,y: 0},
	R2D = 180 / Math.PI,
	rot = document.getElementById('rotate');

	init = function() {
		rot.addEventListener("mousedown", start, false);
		$(document).bind('mousemove', function(event) {
			if (active === true) {
				event.preventDefault();
				rotate(event);
			}
		});
		$(document).bind('mouseup', function(event) {
			event.preventDefault();
			stop(event);
		});
	};

	start = function(e) {
		e.preventDefault();
		var bb = this.getBoundingClientRect(),
		t = bb.top,
		l = bb.left,
		h = bb.height,
		w = bb.width,
		x, y;
		center = {x: l + (w / 2), y: t + (h / 2)};
		x = e.clientX - center.x;
		y = e.clientY - center.y;
		startAngle = R2D * Math.atan2(y, x);
		return active = true;
	};

	rotate = function(e) {
		e.preventDefault();
		var x = e.clientX - center.x,
		y = e.clientY - center.y,
		d = R2D * Math.atan2(y, x);
		rotation = d - startAngle;

		let val = angle + rotation % 360;
		if (val < 0) {
			val = 360 + val;
		}
		val = (val / 360) * 255;
		$('#rotate-value').val(Math.round(val));

		return rot.style.transform = "rotate(" + (angle + rotation) + "deg)";
	};

	stop = function() {
		angle += rotation;
		return active = false;
	};

	init();

}).call(this);