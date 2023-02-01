$(document).ready(() => {
  $(".btn").click(() => {
    $.ajax({
      url: "",
      type: "get",
      data: {
        button_text: $(this).text(),
      },
      success: (response) => {
        // $(".btn").text(response.seconds);
        $("#seconds").append(`<li>${response.seconds}</li>`);
      },
    });
  });
});

function getAllTodos(url) {
  fetch(url, {
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const todoList = document.getElementById("todoList");
      todoList.innerHTML = "";

      data.context.forEach((todo) => {
        const todoHTMLElement = `
        <li>
          <p>Task: ${todo.task}</p>
          <p>Completed?: ${todo.completed}</p>
        </li>`;
        todoList.innerHTML += todoHTMLElement;
      });
    });
}

function addTodo(url, payload) {
  fetch(url, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({ payload: payload }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });
}

function updateTodo(url, payload) {
  fetch(url, {
    method: "PUT",
    credentials: "same-origin",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({ payload: payload }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });
}

function deleteTodo(url) {
  fetch(url, {
    method: "DELETE",
    credentials: "same-origin",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });
}
