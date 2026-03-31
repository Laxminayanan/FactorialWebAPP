const form = document.getElementById("factorialForm");
const loading = document.getElementById("loading");
const input = document.getElementById("numberInput");

form.addEventListener("submit", function () {
    loading.classList.remove("hidden");
});

/* CLIENT SIDE VALIDATION */
input.addEventListener("input", function () {
    if (isNaN(input.value)) {
        input.style.border = "2px solid red";
    } else {
        input.style.border = "none";
    }
});

/* COPY FUNCTION */
function copyResult() {
    const text = document.querySelector(".result").innerText;
    navigator.clipboard.writeText(text);
    alert("Copied to clipboard!");
}
