// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $dateTimeinput = document.querySelector("#dateTime");
var $searchBtn = document.querySelector("#search");
// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.onclick = handleSearchButtonClick;
// Set filteredAddresses to addressData initially
var filteredAliens = dataSet;
// renderTable renders the filteredAddresses to the tbody
function renderTable() {
//   $tbody.innerHTML = "";
  for (var i = 0; i < dataSet.length; i++) {
    // Get get the current address object and its fields
    var sighting= dataSet[i];
    var fields = Object.keys(sighting);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the address object, create a new cell at set its inner text to be the current value at the current address's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = sighting[field];
    }
    
  }
}
function handleSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterdate = $dateTimeinput.value.trim();
  filtereddateTimes = filteredAliens.filter(function(date) {
    var date_time = date.datetime;
    return date_time === filterdate;
  });
  renderTable();
}
// Render the table for the first time on page load
renderTable();