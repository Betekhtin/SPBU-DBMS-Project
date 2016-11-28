$(document).ready(function() {
  var table = $("table");
  var rows = table.find("tr");
  for(var i = 1; i < rows.length; ++i){
    var row = $(rows[i]);
    var time = row.find(".time").text();
    if (time >= "07:00:00" && time < "21:00:00") row.addClass("day");
    else row.addClass("night");
  }
});
