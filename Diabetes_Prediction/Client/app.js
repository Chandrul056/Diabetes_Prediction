function onClickedEstimatePrice(){
    
    console.log("Estimate Price Button Clicked");
    
    var preg = document.getElementById("uipreg");
    var glu = document.getElementById("uiglu");
    var blo = document.getElementById("uibp");
    var ski = document.getElementById("uist");
    var ins = document.getElementById("uiins");
    var bod = document.getElementById("uibmi");
    var dia = document.getElementById("uidpf");
    var age = document.getElementById("uiag");
    
    var estPrice = document.getElementById("uiEstimatedPrice");
    
    var url = "http://127.0.0.1:5000/predict";
    
    //var url ="/api/predict";
    
    $.post(url,{
        pregnancies: parseInt(preg.value),
        glucose: parseInt(glu.value),
        bloodpressure: parseInt(blo.value),
        skinthickness: parseInt(ski.value),
        insulin: parseInt(ins.value),
        bodymassindex: parseFloat(bod.value),
        diabetespedigreefunction: parseFloat(dia.value),
        age: parseInt(age.value)
        
    },function(data, status){
        console.log(data);
        estPrice.innerHTML = "<h2>" + data.toString() + "</h2>";
        console.log(status);
    });
    
}