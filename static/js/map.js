function getLocation() {
    // console.log("geolocation" in navigator);
    if ("geolocation" in navigator) {

        navigator.geolocation.getCurrentPosition(position => {
            const lat = position.coords.latitude;
            const long = position.coords.longitude;
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
                    center: ol.proj.fromLonLat([long, lat]),
                    zoom: 15
                })
            });
            var searchBtn = document.getElementById("search-btn");
            searchBtn.addEventListener("click", function () {
                const attr = document.querySelectorAll(".attr-box.clicked")[0];
                if (attr) {
                    const xhr = new XMLHttpRequest();
                    xhr.onload = () => console.log(xhr.response);
                    xhr.responseType = "JSON";
                    xhr.open("GET", `/api/${attr.dataset.id}?lat=${lat}&lon=${long}&time=${new Date().getTime()}&attribute=${attr.dataset.type}`);
                    xhr.send();
                }
            }, error);
        });
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