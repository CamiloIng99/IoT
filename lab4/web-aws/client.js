const jsonText = document.getElementById("demo");
const button1=document.getElementById("button1");

var myInterval;
var flag=false;


button1.onclick=function(){

if(flag==false){
myInterval=setInterval(function() {jsonText.innerHTML = httpGet("https://krvz8muixk.execute-api.us-east-1.amazonaws.com/test/data")}, 10000);

button1.innerText="Stop";
flag=true;
}
else{
    clearInterval(myInterval);
    button1.innerText="Start";
    jsonText.innerText="";
    flag=false;
}

}

// Synchronous implementation
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
   
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request    
    xmlHttp.send( );    

    return xmlHttp.responseText;
}

// Asynchronous implementation
function httpGetAsync(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
   
    
    // onload is a function
    xmlHttp.onload = function() {
    jsonText.innerHTML =this.responseText;
  }
    xmlHttp.open( "GET", theUrl, true ); // true for asynchronous request        
    xmlHttp.send( );

    
}