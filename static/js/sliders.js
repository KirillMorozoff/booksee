var rev_from = "20000";
var rev_to = "170000";

        $(function() {

           $( "#slider-5" ).slider({
              range:true,
              min: 0,
              max: 200000,
              values: [ rev_from, rev_to ],
              slide: function( event, ui ) {
                 $( "#price5" ).val( "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
              }
           });
           $( "#price5" ).val( "" + $( "#slider-5" ).slider( "values", 0 ) +
              " - " + $( "#slider-5" ).slider( "values", 1 ) );
        });


var rate_from = "20000";
var rate_to = "170000";

        $(function() {

           $( "#slider-4" ).slider({
              range:true,
              min: 0,
              max: 200000,
              values: [ rate_from, rate_to ],
              slide: function( event, ui ) {
                 $( "#price4" ).val( "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
              }
           });
           $( "#price4" ).val( "" + $( "#slider-4" ).slider( "values", 0 ) +
              " - " + $( "#slider-4" ).slider( "values", 1 ) );
        });


        var rating_from = "1.5";
        var rating_to = "3.5";

                $(function() {

                   $( "#slider-3" ).slider({
                      range:true,
                      min: 0,
                      max: 5,
                      step: 0.1,
                      values: [ rating_from, rating_to ],
                      slide: function( event, ui ) {
                         $( "#price3" ).val( "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
                      }
                   });
                   $( "#price3" ).val( "" + $( "#slider-3" ).slider( "values", 0 ) +
                      " - " + $( "#slider-3" ).slider( "values", 1 ) );
                });



                var pages_from = "650";
                var pages_to = "1300";

                        $(function() {

                           $( "#slider-2" ).slider({
                              range:true,
                              min: 0,
                              max: 2000,
                              values: [ pages_from, pages_to ],
                              slide: function( event, ui ) {
                                 $( "#price2" ).val( "" + ui.values[ 0 ] + " - " + ui.values[ 1 ] );
                              }
                           });
                           $( "#price2" ).val( "" + $( "#slider-2" ).slider( "values", 0 ) +
                              " - " + $( "#slider-2" ).slider( "values", 1 ) );
                        });
