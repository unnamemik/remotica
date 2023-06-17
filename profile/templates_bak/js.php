<!DOCTYPE html>
<head>
    <style type="text/css">
        body {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: #222;
        }

        main {
            max-width: 600px;
        }

        .input-group {
            margin: 1rem;
        }

        .list-group {
            min-height: 100px;
            height: 100%;
        }

        .list-group-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        div + div {
            border-right: 1px dotted #222;
        }

        h3 {
            text-align: center;
        }

        p {
            margin: 0;
        }

        .completed p {
            text-decoration: line-through;
        }

        .in-progress p {
            border-bottom: 1px dashed #222;
        }

        .drop {
            background: linear-gradient(#eee, transparent);
            border-radius: 4px;
        }

    </style>



</head>
<body><h1>Drag & Drop</h1>
<main class="row">
    <div class="input-group">
        <div class="input-group-prepend">
            <span class="input-group-text">Enter new todo: </span>
        </div>
        <input type="text" class="form-control" placeholder="todo4" data-name="todo-input" />
        <div class="input-group-append">
            <button class="btn btn-success" data-name="add-btn">Add</button>
        </div>
    </div>

    <div class="col-4">
        <h3>Todos</h3>
        <ul class="list-group" data-name="todos-list">
            <li class="list-group-item" data-id="1" draggable="true">
                <p>todo1</p>
                <button class="btn btn-outline-danger btn-sm" data-name="remove-btn">
                    X
                </button>
            </li>
            <li class="list-group-item" data-id="2" draggable="true">
                <p>todo2</p>
                <button class="btn btn-outline-danger btn-sm" data-name="remove-btn">
                    X
                </button>
            </li>
            <li class="list-group-item" data-id="3" draggable="true">
                <p>todo3</p>
                <button class="btn btn-outline-danger btn-sm" data-name="remove-btn">
                    X
                </button>
            </li>
        </ul>
    </div>

    <div class="col-4">
        <h3>In Progress</h3>
        <ul class="list-group" data-name="in-progress-list"></ul>
    </div>

    <div class="col-4">
        <h3>Completed</h3>
        <ul class="list-group" data-name="completed-list"></ul>
    </div>
</main>
</body>
</html>


<script type="text/javascript">
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

</script>