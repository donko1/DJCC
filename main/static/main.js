function sleep(time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

const container = document.getElementsByClassName("container")[0];

setInterval(() => {
  const elems = Array(document.getElementsByClassName("elem"));
  const newElems = new Array();
  elems[0][1].classList.remove("main__elem");
  newElems[1] = elems[0][2];
  newElems[2] = elems[0][0];
  newElems[0] = elems[0][1];

  elems[0][2].classList.add("move-up");
  elems[0][1].classList.add("move-up");
  elems[0][2].classList.add("main__elem");
  elems[0][0].classList.add("move-down");
  sleep(1000).then(() => {
    elems[0][2].classList.remove("move-up");
    elems[0][1].classList.remove("move-up");
    elems[0][0].classList.remove("move-down");

    container.replaceChild(newElems[0], elems[0][0]);
    container.replaceChild(newElems[1], elems[0][1]);
    container.appendChild(newElems[2]);
  });
}, 7000);

// function getLang() {
//   const cookie = document.cookie
//     .split("; ")
//     .find((row) => row.startsWith(`lang=`));
//   return cookie ? cookie.split("=")[1] : "en";
// }
// function CWBL(en_v, ru_v, lang) {
//   switch (lang) {
//     case "ru":
//       return ru_v;
//     case "en":
//       return en_v;
//   }
// }

// function useCookie(cookieName, defaultValue) {
//   let value = localStorage.getItem(cookieName) || defaultValue;

//   const setCookieValue = (newValue) => {
//     localStorage.setItem(cookieName, newValue);
//     value = newValue;
//   };

//   return [value, setCookieValue];
// }


// function LanguageButton() {
//   const [value, setValue] = useCookie("lang", "en");

//   const changeLang = (newValue) => {
//     setValue(newValue);
//   };
//   const ruB = document.createElement("button")
//   const enB = document.createElement("button")
//   ruB.textContent = "Ru"
//   enB.textContent = "En"
//   var div = document.createElement("div")
//   div.classList.add("langButtons")
//   enB.addEventListener("click", () => changeLang("en"))
//   ruB.addEventListener("click", () => changeLang("ru"))
//   if (value === "en"){
//     div.appendChild(enB)
//   }
//   else {
//     div.appendChild(ruB)
//   }
//   return div
// }


// document.getElementsByClassName("parallax-content")[0].appendChild(LanguageButton())