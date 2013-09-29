jQuery(function ($) {
    var reddoid = {};
    if (this.reddoid !== undefined) {
        reddoid = this.reddoid;
    } else {
        this.reddoid = reddoid;
    }
    reddoid.home = {
        page: 1,
        init:function () {
            $(window).scroll(function() {
                if($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
                    reddoid.home.next_page();
                }
            });
            reddoid.home.next_page();
        },
        next_page:function() {
            $.ajax({
                url: $('.sidebar').data('posts-url'),
                dataType: 'json',
                data: {date: $('.sidebar').data('date'), page: reddoid.home.page},
                type: 'GET',
                success: function (data) {
                    if(data['posts'].length) {
                        for(var i=0; i<data['posts'].length; i++) {
                            console.log(data['posts'][i])
                            $('.js-posts').append('<div class="post"> '+ data['posts'][i]['content'] + '</div>');
                        };
                    }
                    reddoid.home.page += 1;
                },
                error: function() {
                },
            });
        },
    };
    reddoid.home.init();
});

