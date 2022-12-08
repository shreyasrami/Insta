$(function(){
    const toggleThemeBtn = document.querySelector('.header__theme-button');
            
    document.onload = setInitialTheme(localStorage.getItem('theme'));
    function setInitialTheme(themeKey) {
        if(themeKey === 'dark') {
            document.documentElement.classList.add('darkTheme');
            document.querySelectorAll('.inverted').forEach((result) => {
                result.classList.toggle('invert');
            })
            $(".caption").css('color','rgb(255,255,255)');
            $(".bio").css('color','rgb(255,255,255)');
            $(".commentemoji").css('background-color','rgb(0,0,0)');
            $(".commentemoji").css('color','rgb(255,255,255)');
            $(".emoji").css('background-color','rgb(0,0,0)');
            $(".emoji").css('color','rgb(255,255,255)');
        }
        else {
            document.documentElement.classList.remove('darkTheme');
        }
        
    }

    toggleThemeBtn.addEventListener('click', () => {

        document.documentElement.classList.toggle('darkTheme');

        if(document.documentElement.classList.contains('darkTheme')) {
            localStorage.setItem('theme', 'dark');
            $(".caption").css('color','rgb(255,255,255)');
            $(".bio").css('color','rgb(255,255,255)');
            $(".commentemoji").css('background-color','rgb(0,0,0)');
            $(".commentemoji").css('color','rgb(255,255,255)');
            $(".emoji").css('background-color','rgb(0,0,0)');
            $(".emoji").css('color','rgb(255,255,255)');
        }
        else {
            localStorage.setItem('theme', 'light');
            $(".caption").css('color','rgb(0,0,0)');
            $(".bio").css('color','rgb(0,0,0)');
            $(".commentemoji").css('background-color','rgb(255,255,255)');
            $(".commentemoji").css('color','rgb(0,0,0)');
            $(".emoji").css('background-color','rgb(255,255,255)');
            $(".emoji").css('color','rgb(0,0,0)');
        }

        document.querySelectorAll('.inverted').forEach((result) => {
            result.classList.toggle('invert');
        });
        
    });
    
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