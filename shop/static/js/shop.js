// Get all modal buttons
var btns = document.getElementsByClassName("see-more");

// Loop through all buttons
for (var i = 0; i < btns.length; i++) {
  // When the user clicks on the button, open the modal
  btns[i].onclick = function () {
    var modal = document.querySelector(this.getAttribute("data-target"));
    modal.style.display = "block";
  };
}

// Get all elements with class="close"
var spans = document.getElementsByClassName("close");

// Loop through all close buttons
for (var i = 0; i < spans.length; i++) {
  // When the user clicks on <span> (x), close the modal
  spans[i].onclick = function () {
    this.parentElement.parentElement.style.display = "none";
  };
}

document.getElementById("loginButton").addEventListener("click", function () {
  document.getElementById("loginPopup").style.display = "flex";
});

document
  .getElementById("loginPopup")
  .addEventListener("click", function (event) {
    if (event.target == this) {
      this.style.display = "none";
    }
  });

document
  .getElementById("logoutForm")
  .addEventListener("submit", function (event) {
    if (!confirm("Are you sure you want to log out?")) {
      event.preventDefault();
    }
  });
