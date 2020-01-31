$(document).on('change', '.sport', function(){
    var team_select = document.getElementById("picks-" + $(this).parents('.subform').data('index') + '-team');
    fetch('/teams/' + this.value).then(function(response,optionHTML){
        response.json().then(function(data, optionHTML){
            var optionHTML = '';

            for (var team of data.teams) {
                optionHTML += '<option value="' + team + '">' + team + '</option>\n';
            }

            team_select.innerHTML = optionHTML;

        });
    });
});
