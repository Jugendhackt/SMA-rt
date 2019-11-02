function getLocation() {
    // console.log("geolocation" in navigator);
    if ("geolocation" in navigator) {

        navigator.geolocation.getCurrentPosition(position => {
            // Loads the map
            console.log(navigator.permissions.query({name: "geolocation"}));
            const map = new ol.Map({
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
    } else console.log("Geolocation not supported");
}

function error() {
    const map = new ol.Map({
        target: 'map',
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ],
        view: new ol.View({
            center: ol.proj.fromLonLat([9, 48]),
            zoom: 4
        })
    });
    console.log("No geolocation permissions")
}

getLocation();