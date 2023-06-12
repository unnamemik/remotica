const main = document.querySelector("main");

    main.addEventListener("click", (e) => {
        if (e.target.tagName === "BUTTON") {
            const { name } = e.target.dataset;
            if (name === "add-btn") {
                const todoInput = main.querySelector('[data-name="todo-input"]');
                if (todoInput.value.trim() !== "") {
                    const value = todoInput.value;
                    const template = `
        <li class="list-group-item" draggable="true" data-id="${Date.now()}">
          <p>${value}</p>
          <button class="btn btn-outline-danger btn-sm" data-name="remove-btn">X</button>
        </li>
        `;
                    const todosList = main.querySelector('[data-name="todos-list"]');
                    todosList.insertAdjacentHTML("beforeend", template);
                    todoInput.value = "";
                }
            } else if (name === "remove-btn") {
                e.target.parentElement.remove();
            }
        }
    });

    main.addEventListener("dragenter", (e) => {
        if (e.target.classList.contains("list-group")) {
            e.target.classList.add("drop");
        }
    });

    main.addEventListener("dragleave", (e) => {
        if (e.target.classList.contains("drop")) {
            e.target.classList.remove("drop");
        }
    });

    main.addEventListener("dragstart", (e) => {
        if (e.target.classList.contains("list-group-item")) {
            e.dataTransfer.setData("text/plain", e.target.dataset.id);
        }
    });

    let elemBelow = "";

    main.addEventListener("dragover", (e) => {
        e.preventDefault();

        elemBelow = e.target;
    });

    main.addEventListener("drop", (e) => {
        const todo = main.querySelector(
            `[data-id="${e.dataTransfer.getData("text/plain")}"]`
        );

        if (elemBelow === todo) {
            return;
        }

        if (elemBelow.tagName === "P" || elemBelow.tagName === "BUTTON") {
            elemBelow = elemBelow.parentElement;
        }

        if (elemBelow.classList.contains("list-group-item")) {
            const center =
                elemBelow.getBoundingClientRect().y +
                elemBelow.getBoundingClientRect().height / 2;

            if (e.clientY > center) {
                if (elemBelow.nextElementSibling !== null) {
                    elemBelow = elemBelow.nextElementSibling;
                } else {
                    return;
                }
            }

            elemBelow.parentElement.insertBefore(todo, elemBelow);
            todo.className = elemBelow.className;
        }

        if (e.target.classList.contains("list-group")) {
            e.target.append(todo);

            if (e.target.classList.contains("drop")) {
                e.target.classList.remove("drop");
            }

            const { name } = e.target.dataset;

            if (name === "completed-list") {
                if (todo.classList.contains("in-progress")) {
                    todo.classList.remove("in-progress");
                }
                let but_command = prompt('Введите команду для кнопки: ');
                todo.textContent = but_command;
                todo.classList.add("completed");
            } else if (name === "in-progress-list") {
                if (todo.classList.contains("completed")) {
                    todo.classList.remove("completed");
                }
                todo.classList.add("in-progress");
            } else {
                todo.className = "list-group-item";
            }
        }
    });


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
		val = (val / 360) * 300;
		if (val > 255) {
			$('#rotate-value').val(0);
		}else{
			$('#rotate-value').val(Math.round(val));
		}

		return rot.style.transform = "rotate(" + (angle + rotation) + "deg)";
	};

	stop = function() {
		angle += rotation;
		return active = false;
	};

	init();

}).call(this);