$(document).ready(function(){
    // Map your teams to your league value
    // When an option is changed, search the above for matching teams
    $('#leagues').on('change', function() {
       // Set selected option as variable
       var selectValue = $(this).val();

       // Empty the target field
       $('#teams').empty();

       // For each chocie in the selected option
       for (i = 0; i < teamnames[selectValue].length; i++) {
          // Output choice in the target field
          $('#teams').append("<option data-tokens= " + teamnames[selectValue][i] + " value='" + teamnames[selectValue][i] + "'>" + teamnames[selectValue][i] + "</option>");
       }
    });
});
