let play = document.querySelector('#play');
    let title = document.querySelector('#title')
    let volumeIco = document.querySelector('#volumeIco');;
    let recent_volume = document.querySelector('#volume');
    let volume_show = document.querySelector('#volume_show');
    let slider = document.querySelector('#duration_slider');
    let show_duration = document.querySelector('#show_duration');
    let track_image = document.querySelector('#track_image');
    let artist = document.querySelector('#artist');
    let playerContainer = document.querySelector('#playerContainer');

    let timer;
    let playing_song = false;

    let track = document.createElement('audio');

    var trackId;

    function load_track(trackId){
      $("#playerContainer").removeClass("hidden");
      $("#playerContainer").addClass("playerVisible");

      clearInterval(timer);
      reset_slider();

      track.src = document.getElementById(trackId).src;
      title.innerHTML = document.getElementById(trackId).name;
      track_image.src = document.getElementById(trackId).alt;

      track.load();
      playsong();
      timer = setInterval(range_slider , 1000);
    }

    let currentVolume = 50;
    function volume_change(){
      volume_show.innerHTML = recent_volume.value;
      track.volume = recent_volume.value / 100;
      currentVolume = recent_volume.value;

      if (currentVolume == 0) {
        mute_sound();
      }else if (currentVolume > 0) {
        unmute_sound();
      }
    }

    function mute_unmute_sound(){
      if (recent_volume.value > 0) {
        mute_sound();
      }else if (recent_volume.value == 0) {
        unmute_sound();
      }
    }

    function mute_sound(){
      track.volume = 0;
      volume.value = 0;
      volume_show.innerHTML = 0;
      volumeIco.innerHTML = '<i class="fa fa-volume-off" aria-hidden="true" id="volume_icon" onclick="mute_unmute_sound()"></i>'
    }
    function unmute_sound(){
      volume.value = currentVolume;
      volume_show.innerHTML = currentVolume;
      track.volume = currentVolume / 100;
      volumeIco.innerHTML = '<i class="fa fa-volume-up" aria-hidden="true" id="volume_icon" onclick="mute_unmute_sound()"></i>'
    }

    function reset_slider(){
      slider.value = 0;
    }

    function justplay(){
      if (playing_song==false) {
        playsong();
      }else {
        pausesong();
      }
    }

    function playsong(){
      track.play();
      playing_song = true;
      play.innerHTML = '<i class="fa fa-pause" aria-hidden="true"></i>';
    }

    function pausesong(){
      track.pause();
      playing_song = false;
      play.innerHTML = '<i class="fa fa-play" aria-hidden="true"></i>';
    }

    function change_duration(){
      slider_position = track.duration * (slider.value / 100);
      track.currentTime = slider_position;
    }

    function range_slider(){
      let position = 0;

      if (!isNaN(track.duration)) {
        position = track.currentTime * (100 / track.duration);
        slider.value = position;
      }
      if (track.ended) {
        clearInterval(timer);
        reset_slider();
        play.innerHTML = '<i class="fa fa-play" aria-hidden="true"></i>';
        $("#playerContainer").removeClass("playerVisible");
        $("#playerContainer").addClass("hidden");
      }
    }
    function dismiss_player(){
      pausesong();
      clearInterval(timer);
      reset_slider();
      play.innerHTML = '<i class="fa fa-play" aria-hidden="true"></i>';
      $("#playerContainer").removeClass("playerVisible");
      $("#playerContainer").addClass("hidden");



    }