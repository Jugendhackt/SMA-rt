document.addEventListener("DOMContentLoaded", () => {
    // Toggle attribute buttons
    const attrBox = document.getElementsByClassName("attr-box");
    for (const attr of attrBox) {
        attr.addEventListener("click", _ => {
            for (const elem of document.getElementsByClassName("clicked"))
                elem.classList.remove("clicked");
            attr.classList.add("clicked");
        });
    }
    // Open/Close Attribute Menu
    const attrBtn = document.getElementById("attribut-btn");
    attrBtn.addEventListener("click", _ => {
        const attrMenu = document.getElementById("attribute-wrapper");
        if (attrMenu.classList.contains("open")) {
            attrMenu.classList.replace("open", "close");
            attrBtn.classList.remove("open");
        } else {
            attrMenu.classList.replace("close", "open");
            attrBtn.classList.add("open");
        }
    });
});

class Search {
    constructor() {
        this.place = "";
        this.attr = [];
    }

    getData(place) {

    }

}