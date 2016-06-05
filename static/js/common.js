$(document).ready(function(){

    var socket = new io.Socket();
    socket.connect();
    socket.on('connect', function() {
        socket.subscribe('calc_channel');
        console.log("Socket connected");
    });

    socket.on('disconnect', function(){
       console.log("Socket disconnected")
    });

    socket.on('message', function(data){
        var logThis = $("#log-calculations");
        logThis.empty();
        for(i=0; i< data.length; i++){
            logThis.append("<div class='log-row'>"+data[i]+"</div>");
        }
    });

    //Validates the equation
    var re = /[^\]\d\(\)+\-*\/,.]+(?=[^\[\]\(\)]*(?:\[|\(|$))/g;
    $("#math-eq").keyup(function(){
        this.value = this.value.replace(re, "");
    });

    $("#calculate").click(function(){
        pushData();
    });

    $(document).keydown( function(event) {
      if (event.which === 13) {
        pushData();
      }
    });

    function pushData(){
        var equation = $('#math-eq').val();
        if (equation){
            var result = eval(equation);
            var userId = $("#userId").val();
            var push_data = {'user_id': userId, 'calculation': equation+" = "+ result};
            socket.send(push_data);
        }
        else {
            $('#math-eq').css("border-color","#ff7950").attr("placeholder", "Enter some data here");
        }
    }
});