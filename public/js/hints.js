var d = document;
var offSetFromCursorY = 15; // y offset of tooltip
var ie = d.all && !window.opera;
var ns6 = d.getElementById && !d.all;
var tipObj, op;

function tooltip(el, txt, id) {
    tipObj = d.getElementById(id);
    if (el.getAttribute("data-title")) {
        txt = el.getAttribute("data-title");
    }
    tipObj.innerHTML = txt;
    op = 0.1;
    tipObj.style.opacity = op;
    tipObj.style.visibility = "visible";
    el.onmousemove = positionTip;
    appear();
}

function hideInfo(el, id) {
    d.getElementById(id).style.visibility = 'hidden';
    el.onmousemove = '';
}

function ieTrueBody() {
    return (d.compatMode && d.compatMode != "BackCompat") ? d.documentElement : d.body
}

function positionTip(e) {
    var curX = (ns6) ? e.pageX : event.clientX + ieTrueBody().scrollLeft;
    var curY = (ns6) ? e.pageY : event.clientY + ieTrueBody().scrollTop;
    var winWidth = ie ? ieTrueBody().clientWidth : window.innerWidth - 20
    var winHeight = ie ? ieTrueBody().clientHeight : window.innerHeight - 20

    var rightEdge = ie ? winWidth - event.clientX : winWidth - e.clientX;
    var bottomEdge = ie ? winHeight - event.clientY - offSetFromCursorY : winHeight - e.clientY - offSetFromCursorY;

    if (rightEdge < tipObj.offsetWidth) tipObj.style.left = curX - tipObj.offsetWidth + "px";
    else tipObj.style.left = curX + "px";

    if (bottomEdge < tipObj.offsetHeight) tipObj.style.top = curY - tipObj.offsetHeight - offSetFromCursorY + "px"
    else tipObj.style.top = curY + offSetFromCursorY + "px";
}

function appear() {
    if (op < 1) {
        op += 0.1;
        tipObj.style.opacity = op;
        tipObj.style.filter = 'alpha(opacity=' + op * 100 + ')';
        t = setTimeout('appear()', 50);
    }
}
