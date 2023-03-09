"use strict";

/*
AJAX notes

For selected text
var conceptName = $('#aioConceptName').find(":selected").text();
For selected value
var conceptName = $('#aioConceptName').find(":selected").val();
aioConceptName - id name

timeout:
##########################
This will make sure that the error callback is fired if the server doesn't respond within a particular time limit.

$.ajax({
    url: "//myapi.com/json",
    dataType: "jsonp",
    timeout: 15000 // adjust the limit. currently its 15 seconds
}).done(function (data) {
    selectText('Id', data.country);
}).fail(function (jqXHR, textStatus, errorThrown) {
    var defaultOption = 'US'
    selectDropdownByText('Id', defaultOption);
    console.log(errorThrown);
});
This will trigger the fail callback when there is no internet as well.
##########################
*/

const QUERY_NAME = "query_name";
const ERROR = "error";
const TREE_NAME = "supplier_parameters_tree";
const TIMEOUT = 15_000; // adjust the limit. currently its 15 seconds

function show_error(error = "") {
  if (typeof error === "string" || error instanceof String) {
    alert(error);
  } else {
    alert("Ошибка сервера.");
  }
}

function download(filename, text) {
  var element = document.createElement("a");
  element.setAttribute(
    "href",
    "data:text/plain;charset=utf-8," + encodeURIComponent(text)
  );
  element.setAttribute("download", filename);

  element.style.display = "none";
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

function downloadOnClick() {
  console.log("downloadOnClick");
  const trim_material_codes = $("#list_codes").val().trim();

  if (trim_material_codes == "") {
    alert("Введите коды артикулов.");
  } else {
    const material_codes = trim_material_codes
      .split("\n")
      .map((s) => s.trim())
      .filter((s) => s != "")
      .sort();

    console.log(material_codes);

    const supplier_id = $("#suppliers_select").find(":selected").val();
    const tree_numbers = $(".tree").simpleTreePicker("val");
    const is_suppliers_selected = $("#suppliers_select").val();
    //   console.log(is_suppliers_selected);

    if (is_suppliers_selected == null) {
      alert("Выберите поставщика.");
    } else {
      console.log(tree_numbers);
      if (tree_numbers.length == 0) {
        alert("Выберите параметры.");
      } else {
        $.ajax({
          url: "get_materials_as_file",
          type: "get",
          data: {
            supplier_id: supplier_id,
            material_codes: material_codes,
            tree_numbers: tree_numbers,
          },
          timeout: TIMEOUT,
        })
          .done((response) => {
            download("data.txt", response);
          })
          .fail((response) => {
            if (response.responseJSON != undefined) {
              const error = response.responseJSON[ERROR];
              show_error(error);
              //   console.log(error);
            } else {
              alert(getErrorMessage(response.status));
            }
          });
      }
    }
  }
}

function clearTree() {
  $(".tree").empty();
}

function setTreeData(data = {}) {
  // clear checked
  //   $(".tree").simpleTreePicker("clear");

  clearTree();

  //   console.log($(".tree").simpleTreePicker("clear"));
  //   console.log($(".tree").simpleTreePicker("val"));
  //   console.log($(".tree").simpleTreePicker("display"));
  //   console.log($(".tree").simpleTreePicker("set"));

  // set new tree
  $(".tree").simpleTreePicker({
    tree: data,
    name: TREE_NAME,
    onclick: function () {
      //   var selected = $(".tree").simpleTreePicker("display");
      //   console.log(selected);
      var vals = $(".tree").simpleTreePicker("val");
      console.log(vals);
    },
  });
}

function getErrorMessage(status) {
  let message = "";
  switch (status) {
    case 0:
      message = "Нет соединения. Проверьте соединение c сервером";
      break;

    case 500:
      message =
        "Cервер столкнулся с неожиданной ошибкой, которая помешала ему выполнить запрос";
      break;

    default:
      message = `Сообщение об ошибке по коду ${status} не реализовано`;
      break;
  }
  return message;
}

function suppliersOnChanged() {
  /* 
    Number - id узла
    Name - имя узла
    Children - дети
  */
  //   const demoData = {
  //     Number: 0,
  //     Name: "Информация по материалу",
  //     Children: [
  //       {
  //         Number: 1,
  //         Name: "Lee",
  //         Children: [
  //           { Name: "Nash", Children: [{ Name: "Tim" }] },
  //           { Name: "Nicole" },
  //           { Name: "Kelly" },
  //         ],
  //       },
  //       { Number: 2, Name: "Alice" },
  //       { Number: 3, Name: "Stanley" },
  //     ],
  //   };
  //   setTreeData(demoData);

  const supplier_id = $("#suppliers_select").find(":selected").val();
  $.ajax({
    url: "get_tree_view_of_supplier_parameters",
    type: "get",
    data: {
      supplier_id: supplier_id, // get selected supplier_id
    },
    timeout: TIMEOUT,
  })
    .done((response, status, jqXHR) => {
      $(".button_input").attr("disabled", false);
      //   console.log(response.json_supplier_tree_params);
      if (response.json_supplier_tree_params != undefined) {
        const data = JSON.parse(response.json_supplier_tree_params);
        setTreeData(data); // update dropdown menu options
      }
    })
    .fail((response, status, errorThrown) => {
      //   console.log(response);
      //   console.log(status);
      //   console.log(errorThrown);

      clearTree(); // if error clear tree of parameters
      $(".button_input").attr("disabled", true);
      //   console.log(response.responseJSON);
      if (response.responseJSON != undefined) {
        const error = response.responseJSON[ERROR];
        show_error(error);
        console.log(error);
        return;
      }

      alert(getErrorMessage(response.status));
    });
}
