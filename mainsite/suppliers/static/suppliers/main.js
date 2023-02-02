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

function downloadOnClick() {
  my_log("downloadOnClick");
  const lines = $("#list_codes")
    .val()
    .trim()
    .split("\n")
    .map((s) => s.trim());
  my_log(lines);
}

function suppliersOnChanged() {
  const supplier_id = $("#suppliers_select").find(":selected").val(); // get selected supplier_id
  $.ajax({
    url: "",
    type: "get",
    data: {
      query_name: "getSuppliersParameters",
      supplier_id: supplier_id,
    },
    success: (response) => {
      my_log(`success suppliersOnChanged(supplier_id=${supplier_id})`);
      my_log(response);
      const json_obj = JSON.parse(response.suppliers);
      my_log(json_obj);
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
      my_log($("#supplier_parameters_select")[0].loadOptions()); // update dropdown menu options
    },
    error: (response) => {
      my_log("error suppliersOnChanged()");
      my_log(response);
    },
  });
}
