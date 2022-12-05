function iniciarContagem() {
    const second = 1000;
    const minute = second * 60;
    const hour = minute * 60;
    const day = hour * 24;

    let meta =  new Date(); 
    let meta2 = new Date(meta.getTime() + 0.5*60000);
    
    const countDown = new Date(meta2).getTime();
    const x = setInterval(
        function() {    
            const now = new Date().getTime(),
            distance = countDown - now;

            document.getElementById("minutes").innerText = Math.floor((distance % (hour)) / (minute));
            document.getElementById("seconds").innerText = Math.floor((distance % (minute)) / second);

            if (distance < 0) {
                clearInterval(x);
                window.location.replace("/naoachou");
            }
    }, 0)
};

function goIndex() {
    window.location.replace("/");
}