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
$(document).on('change', '.linetype', function(){
    // var line_select = document.getElementById("picks-" + $(this).parents('.subform').data('index') + '-line');
    var $line = $('#picks-'+$(this).parents('.subform').data('index') + '-line');
    var $linetype = $('#picks-'+$(this).parents('.subform').data('index') + '-linetype');

    switch($linetype.val()){
        case 'Spread':
            $line.parent().css('visibility','visible');
            $line.val('');
            $line.attr('pattern','(^[-+]?[1-9]\\d*(\\.5)?$)');
            $line.parent().children('.invalid-feedback').html('Invalid Spread: e.g. 34, -3.5, +3 ')
        break;

        case 'Over/Under':
            $line.parent().css('visibility','visible');
            $line.val('');
            $line.attr('pattern','(^[ou][1-9]\\d*(.5)?$)');
            $line.parent().children('.invalid-feedback').html('Invalid Over/Under: e.g. o34, u3.5')
        break;

        case 'MoneyLine':
            $line.val('0');
            $line.parent().css('visibility', 'hidden');
        break;
    };

});
