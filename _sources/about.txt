.. about reddoid project

About
=====

Reddoid is a mixture of `Reddit <http://en.wikipedia.org/wiki/Reddit>`__ and `Planet <http://en.wikipedia.org/wiki/Planet_%28software%29>`__ social media patterns.

Moderators may add multiple social accounts. Posts from them are shown. Anybody may vote on any post. Posts with most votes get to the main page for a day. Machine learning algorthms are used to predict popular posts.

Posts from multiple social services can be shown: Twitter, Instagram, Facebook, Google+, Github etc. RSS/Atom feeds are also supported.

User stories (not everything is implemented)
============================================

On the home page a user sees links mentioned by a selected group of users in various social networks during the last day. There are navigation links to Images, Videos, Events, Code interactions, Raw posts. Pagination is within a day and to other days. A link where all sources can be seen on one page.

Adding people/sources
---------------------

Moderators may add a source to the group by specifying URL to a profile (Twitter, Google+, Facebook, Vkontakte, Instagram, Flickr, Youtube, Vimeo, Github, Bitbucket). Several sources may be linked to a person, for instance a person may have Twitter, Google+ and Instagram accounts.

Syncing with native lists
-------------------------

All sources are synced with native implementation of lists for a given service (for now only for Twitter lists and Google+ circles). For example, all sources that are added to the service are also added to a list on Twitter, if somebody is removed from the service, he is removed from the list. Same is true if a source is added to the list on Twitter, then it appears on the service.

Voting 
------

One may vote from -1 to +2 (see http://donetskogram.com/). Posts are ordered by score. Votes from different users have different weight and contribute to score differently. Actions on posts in native network (likes, favorites, re-posts etc.) increase their scores too.

Score prediction
----------------

See how it’s done in `photoplanet <https://github.com/dudarev/photoplanet/blob/master/photoplanet/photoplanet/models.py#L26>`__ .

Entities
--------

    - Links (Similar to Hacker News. Elements of interface: title, domain, score, time posted)
    - Images (Similar to http://donetskogram.com/. In addition to Instagram include Flickr, image links from Twitter. Think how to handle Google+ images)
    - Video (Youtube and Vimeo)
    - Code (Bitbucket and Github. Forking, committing etc.)
    - Events (Events can be added manually)
    - Feed of everything
    - Just everything together
    - Weekly .A text that can be collaboratively edited. Posts may be added to weekly with some easy interface. Integration with Mailchimp.

Inspirations
------------

    - http://www.reddit.com
    - http://habrahabr.ru/
    - http://planet.python.org/
    - http://www.planetplanet.org/
    - http://donetskogram.com/
    - https://news.ycombinator.com/
    - http://hckrnews.com/
    - http://www.inbound.org/
