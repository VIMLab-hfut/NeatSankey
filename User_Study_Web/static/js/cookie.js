/**
 * 写入 cookie
 * @param key
 * @param val
 * @param time  天数（1 = 1天）
 */
function setCookie(key, val, time) {
	var date = new Date();
	var expiresDays = time ? time : 7;
	date.setTime(date.getTime() + expiresDays * 24 * 3600 * 1000);
	document.cookie = key + "=" + escape(val) + ";expires=" + date.toGMTString() + ";path=/";
}

/**
 *  读取 cookie
 * @param key
 * @returns {string}
 */
function getCookie(key) {
	var getCookie = document.cookie.replace(/[ ]/g, "");
	var arrCookie = getCookie.split(";")
	var tips;
	for (var i = 0; i < arrCookie.length; i++) {
		var arr = arrCookie[i].split("=");
		if (key == arr[0]) {
			tips = arr[1];
			break;
		}
	}
	return tips;
}

/**
 * 删除 cookie
 * @param key
 */
function delCookie(key){
	var date = new Date(); //获取当前时间
	date.setTime(date.getTime() - 10000); //将date设置为过去的时间
	document.cookie = key + "=v; expires =" + date.toGMTString() + ";path=/"; //设置cookie
	// document.cookie = key + "=v; expires =" + date.toGMTString() + ";path=/;domain=.xunjiecad.com"; //设置cookie
}