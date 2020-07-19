$(function(){
    
    $(document).on('click',".delcmt",function(){
        window.location.replace($(this).data('url'))
    })
    
    $('.dbc').dblclick(function(){
        var id = $(this).attr('name')
        $('#icon_'+id).addClass('effect').show()
        setTimeout(function(){
            $('#icon_'+id).removeClass('effect').hide()
        },800)
    })

    $('.profile').click(function(){
        window.location = $(this).data('url')
    })

    $(".emoji").emojioneArea({
        pickerPosition: "bottom",
        searchPosition: "bottom"
    })
    $(".commentemoji").emojioneArea({
        
        searchPosition: "bottom"
    })


    var username = []
    $.ajax({
        url: $('.search').data('url'),
        dataType: 'json',
        success: function(data){
            $.each(data.name,function(i,v){
                username.push(v)
            })
        }
    })
    $('.search').click(function(){
        $(this).autocomplete({
            source: username
        },
        {
            autoFocus:true
        
        })
    })
    $('.search').keypress(function(event){
        if(event.which == 13){
            $('.frm').submit()
        }
    })

})