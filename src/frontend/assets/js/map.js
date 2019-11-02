function getLocation() {
    //console.log("geolocation" in navigator);
    if ("geolocation" in navigator) {

        navigator.geolocation.getCurrentPosition(function (position) {
            //Loads the map
            console.log(navigator.permissions.query({name: "geolocation"}));
            var map = new ol.Map({
                target: 'map',
                layers: [
                    new ol.layer.Tile({
                        source: new ol.source.OSM()
                    })
                ],
                view: new ol.View({
                    center: ol.proj.fromLonLat([position.coords.longitude, position.coords.latitude]),
                    zoom: 15
                })
            });
        }, error);
    } else {
        //Loads the maponst
        console.log("Geolocation not supported");
    }
}

function error() {
    var map = new ol.Map({
        target: 'map',
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ],
        view: new ol.View({
            center: ol.proj.fromLonLat([51, 13]),
            zoom: 4
        })
    });
    console.log("No geolocation permissions")
}

console.log(Navigator.permission);
getLocation();
console.log(Navigator.permission);