$(document).ready(function() {
    
    var startTime;
    var endTime;
    

    $("#showInput").click(function(){
        $("input[name*='startTime']").val(startTime);
        $("input[name*='endTime']").val(endTime);
    
    });
    
    
    //Table drag select from http://jsfiddle.net/Brv6J/3/
    $(function () {
        var isMouseDown = false,
        isHighlighted;
        var daySelected;
        
        $("#calendar td").mousedown(function () {
        if($(this).hasClass("available")){
            isMouseDown = true;
            startTime = $( this ).attr('id');
            endTime = $(this).attr('id');
            daySelected = $(this).attr('headers');
            $(".highlighted").toggleClass("highlighted");
            $(this).toggleClass("highlighted");
            isHighlighted = $(this).hasClass("highlighted");
            return false; // prevent text selection
            }
    }).mouseover(function () {
    if($(this).hasClass("reserved")){
        isMouseDown = false;
      }
      else if (isMouseDown && $(this).attr('headers') == daySelected  && !$(this).hasClass("highlighted")) {
        $(this).toggleClass("highlighted", isHighlighted);
        endTime = $(this).attr('id');
      }
      
    })
    .bind("selectstart", function () {
      return false;
    })

    $(document)
    .mouseup(function () {
        isMouseDown = false;
        $("input[name*='startTime']").val(startTime);
        $("input[name*='endTime']").val(endTime);
    });
    });
    
    
    
    
    
    
    
    
    
});