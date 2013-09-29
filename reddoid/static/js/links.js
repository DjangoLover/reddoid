jQuery(function ($) {
    var reddoid = {};
    if (this.reddoid !== undefined) {
        reddoid = this.reddoid;
    } else {
        this.reddoid = reddoid;
    }
    reddoid.home = {
        page: 1,
        busy: false,
        init:function () {
            $(window).scroll(function() {
                if($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
                    reddoid.home.next_page();
                }
            });
            reddoid.home.next_page();
            $(document).on('click', '.vote-button .up', function() {
                console.log('up');
            });
            $(document).on('click', '.vote-button .down', function() {
                console.log('down');
            });
        },
        build_post:function(link) {
            return '<div class="post"><div class="vote-button"><span class="up"></span><span class="down"></span></div>' + link['url'] + '</div>'
        },
        next_page:function() {
            if(reddoid.home.busy) return;
            $.ajax({
                url: $('.js-posts').data('links-url'),
                dataType: 'json',
                data: {date: $('.js-posts').data('date'), page: reddoid.home.page},
                type: 'GET',
                success: function (data) {
                    if(data['entities'].length) {
                        for(var i=0; i<data['entities'].length; i++) {
                            $('.js-posts').append(reddoid.home.build_post(data['entities'][i]));
                        };
                    }
                    reddoid.home.page += 1;
                    reddoid.home.busy = false;
                },
                error: function() {
                    reddoid.home.busy = false;
                },
            });
            reddoid.home.busy = true;
        },
    };
    reddoid.home.init();
});

