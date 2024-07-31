function showPd(){
    document.getElementById("pd-btn").style.backgroundColor = "#737272";    
    document.getElementById("pd-btn").style.color = "#393940";    
    document.getElementById("edu-btn").style.backgroundColor = "#393940";
    document.getElementById("edu-btn").style.color = "#737272";
    document.getElementById("edu").style.display = " none"    
    document.getElementById("pd").style.display = "block"

}
function showEdu(){
    document.getElementById("pd-btn").style.backgroundColor = "#393940";    
    document.getElementById("pd-btn").style.color = "#737272";    
    document.getElementById("edu-btn").style.backgroundColor = "#737272";
    document.getElementById("edu-btn").style.color = "#393940";
    document.getElementById("edu").style.display = " block"    
    document.getElementById("pd").style.display = "none"

}