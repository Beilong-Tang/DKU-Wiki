


// bind the data received to the data on the page
function setData(_this, data, args){


  for (var i = 2; i < arguments.length; i++){
    _this[arguments[i]] = data[arguments[i]]
  }

}


function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
      return (arr[2]);
    else
      return null;
  }

function changeStyle(ifEdit){
    if (ifEdit){
      var toolbar = document.getElementsByClassName("ql-toolbar")[0];
      toolbar.style.display='block';
      var content = document.getElementById("content");
      content.style.border='1px solid #ccc'
      content.style.borderTop='0px';
      return;
    }
    else{
      var toolbar = document.getElementsByClassName("ql-toolbar")[0];
      toolbar.style.display='none';
      var content = document.getElementById("content");
      content.style.border='0px';
    }

}


var csrftoken=""

export {
    csrftoken,
    getCookie,
    changeStyle,
    setData
};
