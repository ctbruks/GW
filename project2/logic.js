
var myMap = L.map("map", {
    center: [38.9072, -77.0369],
    zoom: 12
    ,
    });

L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +"access_token=pk.eyJ1Ijoia2pnMzEwIiwiYSI6ImNpdGRjbWhxdjAwNG0yb3A5b21jOXluZTUifQ." + "T6YbdDixkOBWH_k9GbS8JQ")
.addTo(myMap);

var geojson_link = "http://data.insideairbnb.com/united-states/dc/washington-dc/2017-05-10/visualisations/neighbourhoods.geojson"

d3.json(geojson_link, function(data){
    d3.csv("data/sentiment_analysis.csv", function(err, score) {
        for (var i=0; i < score.length; i++){       

            for (var j = 0; j< data.features.length; j++) {
                if (data.features[j].properties.neighbourhood[j] == score[j].neighbourhood_cleansed){
                    data.features[j].properties.sentiment_score = +score[j].sentiment_score;
                }

                L.choropleth(data, {
                    valueProperty:"sentiment_score",
                    // Color scale
                    scale: ["#fff7bc", "#d95f0e"],
                    // Number of breaks in step range
                    steps: 10,
                    mode: "q",
                    style: {
                    // Border color
                    color: "white",
                    dashArray: 2,
                    weight: 1,
                    fillOpacity: 0.8
                    }}).addTo(myMap);
            }
        }
    })
})



