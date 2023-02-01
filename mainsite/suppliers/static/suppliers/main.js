"use strict";

const IS_DEBUG = true;

function my_log(text) {
  if (IS_DEBUG) {
    console.log(text);
  }
}

$(document).ready(() => {
  $(".btn").click(() => {
    $.ajax({
      url: "",
      type: "get",
      data: {
        query_name: "test",
      },
      success: (response) => {
        // $(".btn").text(response.seconds);
        $("#seconds").append(`<li>${response.seconds}</li>`);
      },
    });
  });
});

function suppliersOnChanged() {
  $.ajax({
    url: "",
    type: "get",
    data: {
      query_name: "getSuppliersParameters",
      supplier_id: "1",
    },
    success: (response) => {
      my_log("suppliersOnChanged() success");
      my_log(response);
      const json_obj = JSON.parse(response.suppliers);
      my_log(json_obj);
      $("#supplier_parameters_data_id").find("option").remove();
      json_obj.forEach((element) => {
        const supplier = element.fields;
        $("#supplier_parameters_data_id").append(
          `<option value=${supplier.supplier}>${supplier.parameter_name}</option>`
        );
      });
    },
    error: (response) => {
      my_log("suppliersOnChanged() error");
      my_log(response);
    },
  });
}

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
