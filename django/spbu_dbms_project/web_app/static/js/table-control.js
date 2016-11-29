$(document).ready(function() {
  var table = $("table");
  var rows = table.find("tr");
  for(var i = 1; i < rows.length; ++i){
    var row = $(rows[i]);
    var date = row.find(".date").text();
    var time = date.split(" ")[5].split(":")[0];
    if (time >= 7 && time < 21)row.addClass("day");
    else row.addClass("night");
  }
});
