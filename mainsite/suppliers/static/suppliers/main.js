"use strict";

/*
AJAX notes

For selected text
var conceptName = $('#aioConceptName').find(":selected").text();
For selected value
var conceptName = $('#aioConceptName').find(":selected").val();

aioConceptName - id name
*/

const QUERY_NAME = "query_name";
const ERROR = "error";
const TREE_NAME = "supplier_parameters_tree";

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
    const selected_tree_ids = $(".tree").simpleTreePicker("val");
    const is_suppliers_selected = $("#suppliers_select").val();
    //   console.log(is_suppliers_selected);

    if (is_suppliers_selected == null) {
      alert("Выберите поставщика.");
    } else {
      console.log(selected_tree_ids);
      if (selected_tree_ids.length == 0) {
        alert("Выберите параметры.");
      } else {
        $.ajax({
          url: "get_materials_as_file",
          type: "get",
          data: {
            supplier_id: supplier_id,
            material_codes: material_codes,
            selected_tree_ids: selected_tree_ids,
          },
          success: (response) => {
            //   console.log(new TextDecoder().decode(response));
            //   console.log(response); // response - binary text
            //   response = String.fromCharCode(response);
            download("data.txt", response);
          },
          error: (response) => {
            const error = response.responseJSON[ERROR];
            show_error(error);
            console.log(error);
          },
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
    success: (response) => {
      $(".button_input").attr("disabled", false);
      //   console.log(response.json_tree_view_supplier_parameters);
      if (response.json_tree_view_supplier_parameters != undefined) {
        const data = JSON.parse(response.json_tree_view_supplier_parameters);
        setTreeData(data); // update dropdown menu options
      }
    },
    error: (response) => {
      clearTree();
      $(".button_input").attr("disabled", true);
      const error = response.responseJSON[ERROR];
      show_error(error);
      console.log(error);
    },
  });
}
