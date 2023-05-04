const form = document.getElementById("form");

form.addEventListener("submit", function (e) {
  e.preventDefault();
  getColors();
});

function getColors() {
  const query = form.elements.query.value;
  fetch("/palette", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      query,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      const { colors } = data;

      const container = document.querySelector(".container");
      createColorBoxes(colors, container);
    });
}

function createColorBoxes(colors, parent) {
  // reset container
  parent.innerHTML = "";

  // create color divs
  for (const color of colors) {
    const div = document.createElement("div");
    div.classList.add("color");
    div.style.backgroundColor = color;
    div.style.width = `calc(100%/ ${colors.length})`;

    // copy color to clipboard
    div.addEventListener("click", function () {
      navigator.clipboard.writeText(color);
    });

    // color HEX text
    const span = document.createElement("span");
    span.innerText = color;
    div.appendChild(span);

    parent.appendChild(div);
  }
}
