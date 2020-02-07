// nav hamburger----
document.addEventListener('DOMContentLoaded', () => {
    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach( el => {
        el.addEventListener('click', () => {

        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');

        });
    });
    }

});

// modal----
class BulmaModal {
	constructor(selector) {
		this.elem = document.querySelector(selector)
		this.close_data()
	}
	
	show() {
		this.elem.classList.toggle('is-active')
		this.on_show()
	}
	
	close() {
		this.elem.classList.toggle('is-active')
		this.on_close()
	}
	
	close_data() {
		var modalClose = this.elem.querySelectorAll("[data-bulma-modal='close'], .modal-background")
		var that = this
		modalClose.forEach(function(e) {
			e.addEventListener("click", function() {
				
				that.elem.classList.toggle('is-active')

				var event = new Event('modal:close')

				that.elem.dispatchEvent(event);
			})
		})
	}
	
	on_show() {
		var event = new Event('modal:show')
	
		this.elem.dispatchEvent(event);
	}
	
	on_close() {
		var event = new Event('modal:close')
	
		this.elem.dispatchEvent(event);
	}
	
	addEventListener(event, callback) {
		this.elem.addEventListener(event, callback)
	}
}

var btn = document.querySelector("#btn")
var mdl = new BulmaModal("#myModal")

btn.addEventListener("click", function () {
	mdl.show()
})

mdl.addEventListener('modal:show', function() {
	console.log("opened")
})

mdl.addEventListener("modal:close", function() {
	console.log("closed")
})

// hide and show div for edit----
function editdiv() {
	var x = document.getElementById("myDIV");
	if (x.style.display === "none") {
	  x.style.display = "block";
	} else {
	  x.style.display = "none";
	}
  }

