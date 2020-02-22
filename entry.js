var $ = require('jquery')
require('bootstrap')
require('bootstrap/dist/css/bootstrap.css')
require('inline-attachment/src/inline-attachment')
require('inline-attachment/src/jquery.inline-attachment')

$(function() {
    $('textarea').inlineattachment({
        uploadUrl: '/images'
    });
});
