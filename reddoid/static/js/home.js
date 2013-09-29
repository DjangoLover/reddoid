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
            $(document).on('click', '.votes a', function() {
                var val = parseInt($(this).parent().find('span').innerText())
                console.log(val);
                return false
                /*
                $.ajax({
                    url: $('.js-posts').data('posts-url'),
                    dataType: 'json',
                    data: {date: $('.js-posts').data('date'), page: reddoid.home.page},
                    type: 'GET',
                    success: function (data) {
                        if(data['posts'].length) {
                            for(var i=0; i<data['posts'].length; i++) {
                                $('.js-posts').append(reddoid.home.build_post(data['posts'][i]));
                            };
                        }
                        reddoid.home.page += 1;
                        reddoid.home.busy = false;
                    },
                    error: function() {
                        reddoid.home.busy = false;
                    },
                });
                */
            });
        },
        build_post:function(post) {
            return '<div class="post">' + post['content'] + '<div class="votes"><a href="#">-2</a> <a href="#">-1</a> (<span clas="js-vote-val">5</span>) <a href="#">+1</a> <a href="#">+2</a></div></div>'
        },
        next_page:function() {
            if(reddoid.home.busy) return;
            $.ajax({
                url: $('.js-posts').data('posts-url'),
                dataType: 'json',
                data: {date: $('.js-posts').data('date'), page: reddoid.home.page},
                type: 'GET',
                success: function (data) {
                    if(data['posts'].length) {
                        for(var i=0; i<data['posts'].length; i++) {
                            $('.js-posts').append(reddoid.home.build_post(data['posts'][i]));
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

