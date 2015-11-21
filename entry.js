var $ = require('jquery')
require('bootstrap')
require('bootstrap/dist/css/bootstrap.css')
require('remark')
require('inline-attachment/dist/inline-attachment')
require('inline-attachment/dist/jquery.inline-attachment')

$(function() {
    $('textarea').inlineattachment({
        uploadUrl: '/images'
    });
});
