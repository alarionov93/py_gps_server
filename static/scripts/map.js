(function(){
	ymaps.ready(init);
    var myMap;
    var shown;

    function init() {
    	myMap = new ymaps.Map("map", {
    		center: [58.010259, 56.234195],
    		zoom: 12
    	}, {
    		autoFitToViewport: 'always'
    	});
      
      // setInterval(function(){
        $.get('/list', function(data) {
          // if (shown != null) {
            // shown.removeFromMap(myMap);
          // }
          var points = [];
          console.log(data);
          for (var i = 0; i < data["points"].length; i++) {
              points.push(new YMaps.GeoPoint(data["points"][i]["lat"], data["points"][i]["lon"]));
          }
          var pts = drawPts(points);
          shown = ymaps.geoQuery(pts).addToMap(myMap).applyBoundsToMap(myMap, {checkZoomRange: true});
        });
      // }, 5000);
    }
})();


function drawPts(a) {
  var myPolyline = new ymaps.Polyline(
    // Указываем координаты вершин ломаной.
    a,
  {
    // не убирать этот блок
    // Описываем свойства геообъекта.
  }, {
    // Задаем опции геообъекта.
    // Отключаем кнопку закрытия балуна.
    balloonCloseButton: true,
    // Цвет линии.
    // strokeColor: color,
    // Ширина линии.
    strokeWidth: 6,
    // Коэффициент прозрачности.
    strokeOpacity: 1
  });

  return myPolyline;
}