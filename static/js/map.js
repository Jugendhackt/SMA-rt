function getLocation() {
    // console.log("geolocation" in navigator);
    if ("geolocation" in navigator) {

        navigator.geolocation.getCurrentPosition(position => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            // Loads the map
            console.log(navigator.permissions.query({name: "geolocation"}));
            const vectorLayer = new ol.layer.Vector({
                source: new ol.source.Vector(),
            });
            const map = new ol.Map({
                target: 'map',
                layers: [
                    new ol.layer.Tile({
                        source: new ol.source.OSM()
                    }),
                    vectorLayer,
                ],
                view: new ol.View({
                    center: ol.proj.fromLonLat([lon, lat]),
                    zoom: 15
                })
            });
            const searchBtn = document.getElementById("search-btn");
            searchBtn.addEventListener("click", _ => {
                const attr = document.querySelectorAll(".attr-box.clicked")[0];
                if (attr) {
                    const xhr = new XMLHttpRequest();
                    xhr.onload = () => {
                        const features = vectorLayer.getSource().getFeatures();
                        features.forEach((feature) => {
                            vectorLayer.getSource().removeFeature(feature);
                        });

                        const data = xhr.response.data;
                        const vectorSource = vectorLayer.getSource();
                        for (const spot of data) {
                            const marker = new ol.Feature(
                                new ol.geom.Point(ol.proj.fromLonLat([spot.lng, spot.lat]))
                            );

                            marker.setStyle(new ol.style.Style({
                                    image: new ol.style.Icon({
                                        anchor: [0.5, 36],
                                        anchorXUnits: "fraction",
                                        anchorYUnits: "pixels",
                                        opacity: 1,
                                        src: '/static/img/alpaca.png',
                                        zIndex: 1,
                                        scale: 0.1
                                    }),
                                    zIndex: 1
                                })
                            );
                            vectorSource.addFeature(marker);
                        }
                    };
                    xhr.responseType = "json";
                    xhr.open("GET", `/api/${attr.dataset.id}?lat=${lat}&lon=${lon}&time=${new Date().getTime()}&attribute=${attr.dataset.type}`);
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
