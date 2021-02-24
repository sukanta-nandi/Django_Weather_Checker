
let activeApi = 'apiairnow';

window.onload = function(){
    api = document.getElementById("apiairnow").innerHTML;
    document.getElementById("current-api").innerHTML = api;

}

function changeApi(clickedid){
    var clickedEle = document.getElementById(clickedid)
    var apiName = clickedEle.innerHTML;
    console.log(apiName)
    
    if(!clickedEle.classList.contains('active')){
        activeEle = document.getElementById(activeApi);
        activeEle.classList.remove('active');

        clickedEle.classList.add('active');
        document.getElementById('current-api').innerHTML = apiName;
        activeApi = clickedid;
    }
}