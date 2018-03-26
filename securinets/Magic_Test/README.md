```javascript
const express = require('express')
const app = express()

function getTimestamp(date) {
    try{
        var x = Math.floor((new Date(date)) / 1000);
        return x;
    } catch( e ){
        return  Math.floor((new Date()) / 1000);
    }
}

function getAsciiCode(str)
{
    var arr1 = [];
    for (var n = 0; n < str.length; n ++) 
     {
        var ascii = Number(str.charCodeAt(n));
        arr1.push(ascii);
     }
    return arr1.join('');
}

app.get('/:username/:birth_day', (req, res) => {
    flag = '************';
    username = req.params.username || '';
    birthDay = req.params.birth_day || '';

    console.log(username);
    console.log(birthDay);
    
    var priority = Math.pow(2, getAsciiCode(username) + getTimestamp(birthDay));
    
    if(priority >= 0) {
        res.send('Hey peasent, no flag for you !!');
    }
    else {
        res.send('Your magical powers have been proven, here is your flag: ' + flag );
    }
});

app.listen(3000, () => console.log('Node Task app listening on port 3000!'));

```
We were give this file. To view flag we need to make sure that priority >= 0 should be false. priority is power of 2 and it can never be negative because 2 is positive. We know that getTimestamp(Date) computes time from " 00:00:00 on 1 January 1970". So using any time before it will return negative value so getAsciiCode(username)+ getTimestamp(birthDay) will turn into a string which is not a number(NaN). Javascript cannot compare a NaN to integer so priority >= 0 will be false and else block is executed.

Flag is alerted as shown in the image

![Alt text](flag.png?raw=true "flag.png")
![Alt text](sol.PNG?raw=true "sol.PNG")
