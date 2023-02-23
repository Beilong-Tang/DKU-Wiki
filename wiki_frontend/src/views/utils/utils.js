import Quill from 'quill'

function setContent(id, content,_this){
    _this.quill= new Quill('#'+id, {
            theme: 'snow',
            readOnly:true,
            // modules: {
            //     "toolbar": false
            // }
            })

    _this.quill.setContents(content)
    // document.getElementById
    var toolbar = document.getElementsByClassName("ql-toolbar")[0];
    toolbar.style.display='none';
}

function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
      return (arr[2]);
    else
      return null;
  }

// function disableEdit(this){

// }


var csrftoken=""

export {
    setContent,
    csrftoken,
    getCookie
};
