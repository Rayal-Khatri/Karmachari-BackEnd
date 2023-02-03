function displayTime()
{
var dateTime = new Date();
var hrs=dateTime.getHours();
var min=dateTime.getMinutes();
var sec=dateTime.getSeconds();
var ses = document.getElementById('sessions');
if(hrs>12)
{
    hrs-=12;
    ses.textContent='PM'
}
else
{
    ses.textContent='AM'
}
document.getElementById('hours').innerHTML=hrs
if(min<10)
    document.getElementById('minutes').innerHTML='0'+ min
else
    {document.getElementById('minutes').innerHTML= min}
if(sec<10)
    {document.getElementById('seconds').innerHTML='0' + sec}
else
    {document.getElementById('seconds').innerHTML=sec}
}
setInterval(displayTime, 10);