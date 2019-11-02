document.addEventListener("DOMContentLoaded", () => {
    const attrBox = document.getElementsByClassName("attr-box");
    for (const attr of attrBox) {
        attr.addEventListener("click", e => {
            if (attr.classList.contains("clicked")) {
                attr.classList.remove("clicked");
            }else{
            attr.classList.add("clicked");
            }
        });
    }
    const attrBtn = document.getElementById("attribut-btn");
    attrBtn.addEventListener("click", function (e) {
        const attrMenu = document.getElementById("attribute-wrapper");
        if(attrMenu.classList.contains("open")){
            attrMenu.classList.remove("open");
            attrBtn.classList.remove("open");
            attrMenu.classList.add("close");
        }else{
            attrMenu.classList.add("open");
            attrMenu.classList.remove("close");
            attrBtn.classList.add("open");
        }
    });
});

