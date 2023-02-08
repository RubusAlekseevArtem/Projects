"use strict";

/*
AJAX notes

For selected text
var conceptName = $('#aioConceptName').find(":selected").text();
For selected value
var conceptName = $('#aioConceptName').find(":selected").val();

aioConceptName - id name
*/

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

function downloadOnClick() {
  console.log("downloadOnClick");
  const trim_material_codes = $("#list_codes").val().trim();

  if (trim_material_codes == "") {
    alert("Введите коды артикулов.");
  } else {
    const material_codes = trim_material_codes.split("\n").map((s) => s.trim());

    console.log(material_codes);

    const supplier_id = $("#suppliers_select").find(":selected").val();

    const selected_lables_suppliers_parameters = $(
      ".multiselect-dropdown-list"
    ).find(".checked>label"); // не filter
    //   console.log(selected_suppliers_parameters.get()); // get - массив результат (он вернет обычный массив элементов DOM)

    const selected_suppliers_parameters = selected_lables_suppliers_parameters
      .get()
      .map((el) => el.textContent);

    //   console.log(selected_suppliers_parameters);

    const is_suppliers_selected = $("#suppliers_select").val();
    //   console.log(is_suppliers_selected);

    if (is_suppliers_selected == null) {
      alert("Выберите поставщика.");
    } else {
      console.log(
        "selected_suppliers_parameters=" + selected_suppliers_parameters
      );
      if (selected_suppliers_parameters.length == 0) {
        alert("Выберите параметры.");
      } else {
        if (selected_suppliers_parameters.includes("Все")) {
          console.log("+");
        } else {
          console.log("-");
          $.ajax({
            url: "",
            type: "get",
            data: {
              query_name: "getMaterialsFile",
              supplier_id: supplier_id,
              material_codes: material_codes,
              suppliers_parameters: selected_suppliers_parameters,
            },
            success: (response) => {
              //   console.log(response.suppliers_parameters);
            },
            error: (response) => {
              //   console.log("error downloadOnClick()");
              //   console.log(response);
            },
          });
        }
      }
    }
  }
}

function suppliersOnChanged() {
  const supplier_id = $("#suppliers_select").find(":selected").val();
  $.ajax({
    url: "",
    type: "get",
    data: {
      query_name: "getSuppliersParameters",
      supplier_id: supplier_id, // get selected supplier_id
    },
    success: (response) => {
      //   console.log(`success suppliersOnChanged(supplier_id=${supplier_id})`);
      console.log(response.suppliers_parameters);
      const json_obj = JSON.parse(response.suppliers_parameters);
      //   console.log(json_obj);
      $("#supplier_parameters_select").find("option").remove(); // remove all options
      json_obj.forEach((element) => {
        const supplier = element.fields;
        $("#supplier_parameters_select").append(
          `<option value=${supplier.supplier}>${supplier.parameter_name}</option>`
        );
      });
      /*
      https://stackoverflow.com/questions/4069982/document-getelementbyid-vs-jquery
      """document.getElementById == jQuery $()?""""
      document.getElementById('contents'); //returns a HTML DOM Object
      var contents = $('#contents');  //returns a jQuery Object
      var contents = $('#contents')[0]; //returns a HTML DOM Object
      */
      $("#supplier_parameters_select")[0].loadOptions(); // update dropdown menu options
    },
    error: (response) => {
      console.log("error suppliersOnChanged()");
      console.log(response);
    },
  });
}
