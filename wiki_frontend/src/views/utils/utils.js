import Quill from 'quill'

function setContent(id, content){
    var editor = new Quill('#'+id, {
            theme: 'snow',
            readOnly:true,
            modules: {
                "toolbar": false
            }
            })

    editor.setContents(content)
    // document.getElementById

}

function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
      return (arr[2]);
    else
      return null;
  }


var csrftoken=""

export {
    setContent,
    csrftoken,
    getCookie
};
