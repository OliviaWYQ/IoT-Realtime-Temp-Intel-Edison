// #  Name:    Maoxin Hou,  Xiren Zhou, Yiqian Wang
// #  UNI:   mh3895,  xz2754,  yw3225
// #  Group Code: MOHA

      // function loadTemp() {
      //       // Load Grove module
      //     var groveSensor = require('jsupm_grove');

      //     // Create the temperature sensor object using AIO pin 0
      //     var temp = new groveSensor.GroveTemp(0);
      //     console.log(temp.name());

      //     // Read the temperature ten times, printing both the Celsius and
      //     // equivalent Fahrenheit temperature, waiting one second between readings
      //     var i = 0;
      //     var waiting = setInterval(function() {
      //             var celsius = temp.value();
      //             var fahrenheit = celsius * 9.0/5.0 + 32.0;
      //             console.log(celsius + " degrees Celsius, or " +
      //                 Math.round(fahrenheit) + " degrees Fahrenheit");
      //             i++;
      //             if (i == 10) clearInterval(waiting);
      //             }, 1000);
      //     return temp.value();
      // }


      google.charts.load('current', {'packages':['gauge']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Label', 'Value'],
          // ['Temp', 23],
          ['Temp', 55],
          // ['Network', 68]
        ]);

        var options = {
          width: 400, height: 120,
          redFrom: 90, redTo: 100,
          yellowFrom:75, yellowTo: 90,
          minorTicks: 5
        };

        var chart = new google.visualization.Gauge(document.getElementById('chart_div'));

        chart.draw(data, options);

        // setInterval(function() {
        //   data.setValue(0, 1, 40 + Math.round(60 * Math.random()));
        //   chart.draw(data, options);
        // }, 13000);
        // setInterval(function() {
        //   data.setValue(0, 1, loadTemp());
        //   chart.draw(data, options);
        // }, 5000);
        // // setInterval(function() {
        //   data.setValue(1, 1, 60 + Math.round(20 * Math.random()));
        //   chart.draw(data, options);
        // }, 26000);
      }