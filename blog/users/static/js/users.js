const HTTP = new XMLHttpRequest();
HTTP.open('GET', 'http://127.0.0.1:8000/get_users')
HTTP.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
HTTP.send()
console.log(jQuery.parseJSON(HTTP.response))
var obj = JSON.parse(HTTP.response)
var tbl=$("<table/>").attr("id","mytable");
$("#user-div").append(tbl);
for(var i=0;i<obj.length;i++)
{
    var tr="<tr>";
    var td1="<td>"+obj[i]["id"]+"</td>";
    var td2="<td>"+obj[i]["name"]+"</td>";
    var td3="<td>"+obj[i]["color"]+"</td></tr>";
    
   $("#mytable").append(tr+td1+td2+td3); 
  
}