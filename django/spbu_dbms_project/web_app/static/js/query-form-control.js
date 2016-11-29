var formControl = function (countries, cities, dates) {

    var countryEl = $("#country");
    for (var i = 0; i < countries.length; ++i) {
        countryEl.append($("<option></option>")
            .attr("value", countries[i].country_id)
            .text(countries[i].country_name));
    }

    var cityEl = $("#city");
    countryEl.change(function() {
        cityEl.children().each(function() {
            if (!$(this).attr("disabled")) this.remove();
        });
        cityEl.val("");
        cities.forEach(function(city) {

            if (city.country_id == countryEl.val()) {

                cityEl.append($("<option></option>")
                    .attr("value", city.city_id)
                    .text(city.city_name));
            }
            cityEl.removeAttr("disabled");
        });
    });

    var dateFromEl = $("#date_from");
    var dateToEl = $("#date_to");
    cityEl.change(function() {

      var cityIndex = cityEl.val() - 1;
      if (dateFromEl.length == 0) {
        dateToEl.children().each(function() {
            if (!$(this).attr("disabled")) this.remove();
        });
        dateToEl.removeAttr("disabled");
        var date = new Date(dates[cityIndex]);
        date = new Date(date.getTime() + 86400000);
        date = date.toJSON().split("T")[0];
        dateToEl.attr("min", date);

      }
      else {

        dateFromEl.removeAttr("disabled");
        dateFromEl.attr("min", "2005-01-01");
        dateFromEl.attr("max", dates[cityIndex]);

        dateToEl.removeAttr("disabled");
        dateToEl.attr("min", "2005-01-01");
        dateToEl.attr("max", dates[cityIndex]);
      }
    })

    dateFromEl.change(function() {
        var dateFrom = dateFromEl.val();
        var dateTo = dateToEl.val();
        dateToEl.attr("min", dateFrom);
        if (dateFrom > dateTo) {
            dateToEl.val(dateFrom);
        }
    });
}

function dateParse (date) {
  var el = date.split(" ");
  var months = ["января", "февраля", "марта", "апреля", "мая",
                "июня", "июля", "августа", "сентября", "октября",
                "ноября", "декабря"];
  var result = el[2] + "-" + (months.indexOf(el[1])+1) + "-";
  result += (el[0] > 9)? el[0] : "0" + el[0];
  return result;
}
