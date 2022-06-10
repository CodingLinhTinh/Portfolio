
document.addEventListener('DOMContentLoaded', function() {

    //1. We need to have current user information
    //2. Call the api view for the portfolio user
    //3. Typewriter effect function 
    var myVar = document.getElementById("myVar").value;
    console.log(myVar, "<- Passed from  Portfolio script");

    userInformation(myVar);
});

function userInformation(username){
    const xhr = new XMLHttpRequest()
    const method = "GET"
    const url = `/api/${username}`
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function(){
        const serverResponse = xhr.response
        const information = serverResponse.information
        console.log("Portfolio Script Info ->", information)
        typewriterData(information);
    }
    xhr.send()
}

function typewriterData(information){
    var strings = [`${information.firstName} ${information.lastName}`]
    var names = `${information.fewWords}`;
    var nameArr = names.split(',')
    // Accessing the individual names
    // alert(nameArr[0]); //Harry
    // alert(nameArr[1]); //John
    // alert(nameArr[nameArr.length - 1]); //Alice
    var i;
    for(i=0; i<nameArr.length ; i++){
        strings.push(`${nameArr[i]}`);
    }
    new Typewriter('#typewriter', {
        strings,
        autoStart: true,
        loop: true,
        cursor: "|"
    });  
    console.log("TypeWriter Strings Info ->", strings)
}

//===================================== Typewriter Effect =========================

