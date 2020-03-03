


function createClock(selector) {
  let container = document.querySelector(selector)
  container.style.color = 'dimgrey'
  container.style.fontSize = '50px'
  let span = document.createElement('span')
  setInterval(function() {
    span.innerText = new Date()
  }, 1000)
  container.appendChild(span)
}