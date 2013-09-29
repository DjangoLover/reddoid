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
                var val = parseInt($(this).text());
                var vote_ind = $(this).parent().find('span');
                var entiti = $(this).parent().parent().find('.entiti > a').attr('href');
                $.ajax({
                    url: $('.js-posts').data('vote-url'),
                    dataType: 'json',
                    data: {val: val, csrfmiddlewaretoken: $('.js-posts').data('csrf'), entiti: entiti},
                    type: 'POST',
                    success: function (data) {
                        if(data['success']) {
                            console.log(vote_ind);
                            vote_ind.text(data['vote']);
                        }
                    },
                });
                return false
            });
        },
        build_post:function(link) {
            return '<div class="post"><div class="entiti"><a href="' + link['url'] + '">' + link['title'] + '</a></div><div class="votes"> <a href="#">-1</a> (<span>' + link['votes'] +'</span>) <a href="#">+1</a> <a href="#">+2</a></div></div>'
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

