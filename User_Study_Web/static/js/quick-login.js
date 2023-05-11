
var t_url = window.location.href;
var qq_link = 'http://vip.cssmoban.com/openlogin/qqlogin?url=' + encodeURIComponent(t_url); // qq快捷登录
var wx_link = 'http://vip.cssmoban.com/openlogin/weixinlogin?url=' + encodeURIComponent(t_url); // 微信快捷登录

var login_html = '<div class="login-box">\n' +
    '    <div class="login">\n' +
    '\n' +
    '        <div class="close-loginbox"></div>\n' +
    '\n' +
    '        <div class="title">\n' +
    '            <p class="title-major">模板之家</p>\n' +
    '            <p class="title-minor"><em></em><span>三秒登录即可下载</span><em></em></p>\n' +
    '        </div>\n' +
    '\n' +
    '        <div class="quick-login">\n' +
    '            <div class="quick-l-wx wxlogin ajaxopen" data-action="' + wx_link + '" data-title="微信登陆" data-w="35%" data-y="50%" id="wxurl">\n' +
    '                <div class="l-wx-icon">\n' +
    '                    <div class="wx-icon"></div>\n' +
    '                </div>\n' +
    '                <p>微信登录</p>\n' +
    '            </div>\n' +
    '            <a class="quick-l-qq qqlogin ajaxopen" href="'+ qq_link +'" data-title="QQ登陆" data-w="35%" data-y="50%">\n' +
    // '            <div class="quick-l-qq qqlogin" data-action="'+ qq_link +'" data-title="QQ登陆" data-w="50%" data-y="50%">\n' +
    '                <div class="l-qq-icon">\n' +
    '                    <div class="qq-icon"></div>\n' +
    '                </div>\n' +
    '                <p>QQ登录</p>\n' +
    '            </div>\n' +
    '        </a>\n' +
    '    </div>\n' +
    '</div>' +
    '<div class="quick-login-ifr-box">' +
        '<div class="quick-login-ifr-title">' +
            '<span class="ifr-title">QQ登录</span>' +
            '<div class="ifr-close"></div>' +
        '</div>' +
        '<iframe src="" frameborder="0" class="quick-login-ifr" id="quick-login-ifr"></iframe>' +
    '</div>';

$("body").append(login_html);

$(".close-loginbox").click(function () {
    $(".login-box").hide();
});

// $(".login > *").click(function (e) {
//     e.stopPropagation();
// });
//
// $(".login-box").click(function () {
//
//     $(this).hide();
// });