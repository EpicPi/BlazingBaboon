  (function() {
    'use strict';
    var video = document.querySelector('video')
      , canvas;
    var arrays = [];
    /**
     *  generates a still frame image from the stream in the <video>
     *  appends the image to the <body>
     */
    function takeSnapshot() {
      var img = document.querySelector('img') || document.createElement('img');
      var context;
      var width = video.offsetWidth
        , height = video.offsetHeight;

      canvas = canvas || document.createElement('canvas');
      canvas.width = width;
      canvas.height = height;

      context = canvas.getContext('2d');
      context.drawImage(video, 0, 0, width, height);
      img.src = canvas.toDataURL('image/png');
      arrays.push(img);
      document.body.appendChild(img);
      for (var count = 0; count<arrays.length; count += 1){
          console.log(arrays[count]);
      }
    }

    // use MediaDevices API
    // docs: https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia
    if (navigator.mediaDevices) {
      // access the web cam
      navigator.mediaDevices.getUserMedia({video: true})
      // permission granted:
        .then(function(stream) {
          video.srcObject = stream;
          video.addEventListener('click', takeSnapshot);
        })
        // permission denied:
        .catch(function(error) {
          document.body.textContent = 'Could not access the camera. Error: ' + error.name;
        });
    }
  })();
