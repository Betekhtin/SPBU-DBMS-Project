var formControl = function (countries, cities, minDate, maxDate) {

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
    if (minDate != null) {
      dateFromEl.attr("min", minDate);
      dateToEl.attr("min", minDate);
    }
    if (maxDate != null) {
      dateFromEl.attr("max", maxDate);
      dateToEl.attr("max", maxDate);
    }

    dateFromEl.change(function() {
        var dateFrom = dateFromEl.val();
        var dateTo = dateToEl.val();
        dateToEl.attr("min", dateFrom);
        if (dateFrom > dateTo) {
            dateToEl.val(dateFrom);
        }
    });
}
