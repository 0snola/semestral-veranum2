function iniciarMapVina(){
    var coord = {lat:-32.984475 ,lng: -71.547783};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 15,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}

function iniciarMapSantiago(){
  var coord = {lat:-33.43080963235248 ,lng: -70.61892614144422};
  var map = new google.maps.Map(document.getElementById('map'),{
    zoom: 15,
    center: coord
  });
  var marker = new google.maps.Marker({
    position: coord,
    map: map
  });
}



