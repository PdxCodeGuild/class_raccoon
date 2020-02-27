
/* JavaScript utility functions */

function randomChoice(array) {
  return array[Math.floor(Math.random()*array.length)]
}

function randomInt(a, b) {
  return a + Math.floor(Math.random()*(b-a) + 1)
}

function shuffle(array) {
  for (let i=0; i<array.length; ++i) {
    let j = randomInt(0, array.length-1)
    let t = array[i]
    array[i] = array[j]
    array[j] = t
  }
}

function fallbackCopyTextToClipboard(text) {
  var textArea = document.createElement("textarea");
  textArea.value = text;
  textArea.style.position="fixed";  //avoid scrolling to bottom
  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    console.log('Fallback: Copying text command was ' + msg);
  } catch (err) {
    console.error('Fallback: Oops, unable to copy', err);
  }

  document.body.removeChild(textArea);
}

function copyToClipboard(text) {
  if (!navigator.clipboard) {
    fallbackCopyTextToClipboard(text);
    return;
  }
  navigator.clipboard.writeText(text).then(function() {
    console.log('Async: Copying to clipboard was successful!');
  }, function(err) {
    console.error('Async: Could not copy text: ', err);
  });
}


function getSelectMultipleValues(select) {
  var r = [];
  for (var i=0; i<select.options.length; i++) {
    let option = select.options[i]
    if (option.selected) {
      r.push(option.value);
    }
  }
  return r;
}


function getSelectedRadioButton(name){
  let radios = document.getElementsByName(name)
  for(let i = 0; i < radios.length; ++i){
    if(radios[i].checked){
      return radios[i].value
    }
  }
  return null
}