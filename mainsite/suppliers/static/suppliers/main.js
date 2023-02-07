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
  const lines = $("#list_codes")
    .val()
    .trim()
    .split("\n")
    .map((s) => s.trim());
  console.log(lines);
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
