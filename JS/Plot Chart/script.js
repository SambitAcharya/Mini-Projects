var chart = AmCharts.makeChart( "chartdiv", {
  "type": "serial",
  "dataLoader": {
    "url": "data.json"
  },
  "rotate": true,
  "pathToImages": "http://www.amcharts.com/lib/images/",
  "categoryField": "company",
  "startDuration": 1,
  "graphs": [ {
    "type": "column",
    "title": "Stock Price",
    "valueField": "value",
    "fillColors": "#ADD981",
    "fillAlphas": 0.8,
    "lineThickness ": 2,
    "lineAlpha": 0.5
  } ]
} );
