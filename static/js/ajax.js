const audio = document.getElementById('audio');
const stationSelect = document.getElementById('stationSelect');

/* LOAD SAVED */

const savedStation =
    localStorage.getItem('radio_station');

const savedTime =
    localStorage.getItem('radio_time');

if(savedStation){

    audio.src = savedStation;

    stationSelect.value = savedStation;

    if(savedTime){
        audio.currentTime = savedTime;
    }
}

/* CHANGE STATION */

stationSelect.addEventListener('change', () => {

    const url = stationSelect.value;

    audio.src = url;

    audio.play();

    localStorage.setItem(
        'radio_station',
        url
    );
});

/* SAVE TIME */

setInterval(() => {

    localStorage.setItem(
        'radio_time',
        audio.currentTime
    );

}, 1000);