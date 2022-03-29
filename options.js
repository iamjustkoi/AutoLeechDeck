$deckOptions.then((options) => {
    options.addHtmlAddon(HTML_PLACEHOLDER, () => setup(options));
});


function setup(options) {
    const storage = options.auxData();
    const deckInput = document.getElementById("leechDeckInput");

    const nightMode = window.location.hash == "#night";

    console.log("::----(" + Date.now() + ")----::");
    var comp_style = getComputedStyle(document.documentElement);
    let fbg = comp_style.getPropertyValue('--frame-bg');
    let brd = comp_style.getPropertyValue('--border');
    let wbg = comp_style.getPropertyValue('--window-bg');
    const root = document.querySelector(':root');
    root.style.setProperty('--frame-bg', fbg);
    root.style.setProperty('--border', brd);
    root.style.setProperty('--window-bg', wbg);

    console.log("fbg: " + fbg + ", brd: " + brd + ", wbg: " + wbg);

    if (nightMode) {
        deckInput.classList.add("night-mode");
        console.log(deckInput.classList.toString());
    }

    deckInput.addEventListener("change", (e) => {

        let inputDeck = deckInput.value;
        storage.update((data) => {
            return {...data, deckKey: inputDeck};
        });

        // const request = new XMLHttpRequest();
        // request.open("POST", '/__init__.py/processInputResult/"' + inputDeck + '"');
        // // request.open("POST", "/processInputResult/" + JSON.stringify(inputDeck));
        // request.onload = () => {
        //     const message = request.responseText;
        //     console.log("msg: " + message);
        // }
        // request.send();


        //   let number = 0;
        //   try {
        //     number = parseInt(numberInput.value, 10);
        //   } catch (err) {}
        // return store.update((data) => {
        //     return { ...data, myNumberKey: number };
        // });
    });
}


