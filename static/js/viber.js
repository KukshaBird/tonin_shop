
const randomNumber = () => {
    return Math.floor(Math.floor(15) * Math.random());
}

const digit = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'];

const getColor = () => {
    let color = '#'
    for (i = 0; i <= 5; i++) {
        color = color.concat(digit[randomNumber()]);
    };
    return color;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function go() {
    while (true) {
        document.getElementById('viber').style.color = getColor();
        await sleep(5000);
    }
}

go();


