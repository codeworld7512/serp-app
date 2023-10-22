// Get elements
var filesList = document.getElementById('uploaded-files');
var input = document.getElementById('dropzone-file');
var submit = document.getElementById('submit');
var messageContainer = document.getElementById('message-container');

// Add event listeners
document.getElementById('dropzone').addEventListener('dragover', function(e) {
  e.preventDefault();
  e.stopPropagation();
  this.classList.add('dragover');
});

document.getElementById('dropzone').addEventListener('dragleave', function(e) {
  e.preventDefault();
  e.stopPropagation();
  this.classList.remove('dragover');
});

document.getElementById('dropzone').addEventListener('drop', function(e) {
  e.preventDefault();
  e.stopPropagation();
  this.classList.remove('dragover');
  var files = e.dataTransfer.files;
  input.files = files;
  var event = new Event('change');
  input.dispatchEvent(event);
});

input.addEventListener('change', function(e) {
  var files = e.target.files;
  for (var i = 0; i < files.length; i++) {
    var file = files[i];
    var li = document.createElement('li');
    li.innerHTML = file.name;
    filesList.appendChild(li);
    submit.removeAttribute('disabled');
    submit.classList.remove('bg-gray-500', 'cursor-not-allowed');
    submit.classList.add('bg-blue-500', 'cursor-pointer');
  }
});

document.getElementById('csv-combiner-form').addEventListener('submit', function(e) {
  e.preventDefault();
  var formData = new FormData(this);

  // Get CSRF token
  var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  fetch('{% url "tools:combine_csv" %}', {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrftoken
    },
    body: formData
  })
    .then((response) => response.blob())
    .then((blob) => {
      var url = window.URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'combined_data.csv';
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
    })
    .catch((error) => console.error(error));
});

function displayMessage(type, msg) {
  var messageElement = document.createElement('div');
  messageElement.classList.add('p-3', 'rounded-lg');
  messageElement.innerHTML = msg;
  if (type === 'success') {
    messageElement.classList.add('bg-green-500', 'text-white');
  } else if (type === 'failure') {
    messageElement.classList.add('bg-red-500', 'text-white');
  } else if (type === 'warning') {
    messageElement.classList.add('bg-yellow-500', 'text-black');
  } else if (type === 'info') {
    messageElement.classList.add('bg-blue-500', 'text-white');
  }
  messageContainer.appendChild(messageElement);
}