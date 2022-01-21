var apikey = "16414702278PBkFQblxgluqPsQP68q72feUVhkfB5X";
var tokenUrl = "https://api.dacast.com/v2/vod?apikey=" + apikey;
var fileSource = 'test/video.mp4';
var callbackUrl = '#';
var uploadUrl = "https://upload.dacast.com";

function getToken(){
  console.log('getting token');
  var formData = new FormData();
  formData.append('source', fileSource);
  formData.append('callback_url', callbackUrl);
  formData.append('upload_type', 'ajax');

  var request = new XMLHttpRequest();
  request.open('POST', tokenUrl);
  request.onreadystatechange = function(ev){
    if(request.readyState === 4){
      console.log(request.responseText);
      uploadFile(request.responseText);
    }
  }
  request.send(formData);
}

function uploadFile(responseText){
  console.log('uploading file');
  var jobj = JSON.parse(responseText);

  var formData = new FormData();
  for(var prop in jobj){
    formData.append(prop, jobj[prop]);
  }
  formData.append('file', fileInputElement.files[0]);

  var request = new XMLHttpRequest();
  request.open('POST', uploadUrl);
  request.upload.onprogress = function(ev){
    console.log(ev.loaded / ev.total*100);
  }
  request.onreadystatechange = function(ev){
    if(request.readyState === 4){
      console.log(request.responseText);
    }
  }
  request.send(formData);
}