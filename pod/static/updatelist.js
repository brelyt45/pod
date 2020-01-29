var sport_select = document.getElementById("sport");
var team_select = document.getElementById("team");

sport_select.onchange = function()  {

    sport = sport_select.value;

    fetch('/teams/' + sport).then(function(response) {

        response.json().then(function(data) {
            var optionHTML = '';

            for (var team of data.teams) {
                optionHTML += '<option value="' + team + '">' + team + '</option>';
            }

            team_select.innerHTML = optionHTML;
        })

    });
}
