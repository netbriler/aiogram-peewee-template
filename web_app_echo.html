<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
    <meta name="format-detection" content="telephone=no"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta name="MobileOptimized" content="176"/>
    <meta name="HandheldFriendly" content="True"/>
    <meta name="robots" content="noindex,nofollow"/>
    <title></title>
    <script src="https://telegram.org/js/telegram-web-app.js?1"></script>
    <script src="https://unpkg.com/bowser@2.4.0/es5.js"></script>
    <script>
        function setThemeClass() {
            document.documentElement.className = Telegram.WebApp.colorScheme;
        }

        Telegram.WebApp.onEvent('themeChanged', setThemeClass);
        setThemeClass();

    </script>
    <style>
        * {
            box-sizing: border-box;
        }

        section {
            -ms-overflow-style: none;
        }

        body {
            font-family: sans-serif;
            background-color: var(--tg-theme-bg-color, #ffffff);
            color: var(--tg-theme-text-color, #222222);
            font-size: 16px;
            margin: 0;
            padding: 0;
            color-scheme: var(--tg-color-scheme);
            border: dashed green 2px;
        }

        #viewportStable, #viewport {
            padding: 2px;
            font-size: 9px;
            color: white;
            position: fixed;
            top: 0;
        }

        #viewportStable {
            left: 0;
            background-color: green;
        }

        #viewport {
            right: 0;
            background-color: silver;
        }

        a {
            color: var(--tg-theme-link-color, #2678b6);
        }

        button {
            display: block;
            width: 100%;
            font-size: 14px;
            margin: 15px 0;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            background-color: var(--tg-theme-button-color, #50a8eb);
            color: var(--tg-theme-button-text-color, #ffffff);
            cursor: pointer;
        }

        button[disabled] {
            opacity: 0.6;
            cursor: auto;
            pointer-events: none;
        }

        section {
            padding: 0 8px;
            text-align: center;
            max-height: calc(var(--tg-viewport-height, 100%) - 4px);
            overflow: scroll;
        }

        p {
            margin: 40px 0 15px;
        }

        ul {
            text-align: left;
        }

        li {
            color: var(--tg-theme-hint-color, #a8a8a8);
        }

        textarea {
            width: 100%;
            box-sizing: border-box;
            padding: 7px;
        }

        pre {
            background: rgba(0, 0, 0, .07);
            border-radius: 4px;
            padding: 4px;
            margin: 7px 0;
            word-break: break-all;
            word-break: break-word;
            white-space: pre-wrap;
            text-align: left;
        }

        .dark pre {
            background: rgba(255, 255, 255, .15);
        }

        .hint {
            font-size: .8em;
            color: var(--tg-theme-hint-color, #a8a8a8);
        }

        .ok {
            color: green;
        }

        .err {
            color: red;
        }

        small {
            font-size: 12px;
        }
    </style>
</head>

<body>

<div id="frame">
    <span id="viewportStable"></span>
    <span id="viewport"></span>
</div>

<section>
    <h1 id="greeting"></h1>

    <div id="buttons">
        <button onclick="webviewExpand();">Expand Webview</button>
        <small>(The window goes fullscreen)</small>
        <button onclick="toggleMainButton(this);">Hide Main Button</button>
        <small>(It hides/shows main button)</small>
        <button id="btnTime" onclick="sendTime();">Send time</button>
        <small id="btnTimeSmall">(The bot will recieve a message with filled <code>web_app_data</code> field)</small>
    </div>

    <h3>Test links</h3>
    <ul>
        <li><a href="?nextpage=1">Regular link #1</a> (opens inside webview)</li>
        <li><a href="https://telegram.org/" target="_blank">target="_blank" link</a> (opens outside webview)</li>
        <li><a href="javascript:window.open('https://telegram.org/');">window.open() link</a> (opens outside
            webview)
        </li>
        <li><a href="https://t.me/like">LikeBot t.me link</a> (opens inside Telegram app)</li>
    </ul>

    <h3>Test permissions</h3>
    <ul>
        <li>
            <a href="javascript:" onclick="return requestLocation();">Request Location</a>
            <span id="locationData"></span>
        </li>
        <li>
            <a href="javascript:" onclick="return requestVideo();">Request Video</a>
            <span id="videoData"></span>
        </li>
        <li>
            <a href="javascript:" onclick="return requestAudio();">Request Audio</a>
            <span id="audioData"></span>
        </li>
    </ul>

    <h3>Init Data (unsafe): </h3>
    <pre id="initDataUnsafe"></pre>
    <h3>Theme Data: </h3>
    <pre id="themeData"></pre>
    <h3>Main Button: </h3>
    <pre id="mainButton"></pre>
    <h3>Browser Info: </h3>
    <pre id="browserInfo"></pre>
</section>

<script type="application/javascript">
    Telegram.WebApp.ready();

    const urlParams = new URLSearchParams(new URL(window.location.href).search);
    if (!urlParams.has('keyboard_button')) {
        document.getElementById('btnTime').remove()
        document.getElementById('btnTimeSmall').remove()

        document.querySelector('#greeting').innerHTML = `Hi, ${Telegram.WebApp.initDataUnsafe.user.first_name}!`;
        document.querySelector('#initDataUnsafe').innerHTML = JSON.stringify(Telegram.WebApp.initDataUnsafe, null, 2);
    }

    document.querySelector('#themeData').innerHTML = JSON.stringify(Telegram.WebApp.themeParams, null, 2);
    document.querySelector('#mainButton').innerHTML = JSON.stringify(Telegram.WebApp.MainButton, null, 2);
    document.querySelector('#browserInfo').innerHTML = JSON.stringify(bowser.getParser(window.navigator.userAgent), null, 2);

    Telegram.WebApp.MainButton
        .setText('CLOSE WEBVIEW')
        .show()
        .onClick(() => {
            webviewClose();
        });

    Telegram.WebApp.onEvent('themeChanged', () => {
        document.querySelector('#themeData').innerHTML = JSON.stringify(Telegram.WebApp.themeParams, null, 2);
    });

    Telegram.WebApp.onEvent('viewportChanged', () => {
        document.querySelector('#viewportStable').innerHTML = `${window.innerWidth} x ${Telegram.WebApp.viewportStableHeight.toFixed(2)} | isExpanded: ${Telegram.WebApp.isExpanded}`;
        document.querySelector('#viewport').innerHTML = `${window.innerWidth} x ${Telegram.WebApp.viewportHeight.toFixed(2)}`;
    });

    function toggleMainButton(el) {
        const mainButton = Telegram.WebApp.MainButton;
        if (mainButton.isVisible) {
            mainButton.hide();
            el.innerHTML = 'Show Main Button';
        } else {
            mainButton.show();
            el.innerHTML = 'Hide Main Button';
        }
    }

    function webviewExpand() {
        Telegram.WebApp.expand();
    }

    function webviewClose() {
        Telegram.WebApp.close();
    }

    function sendTime() {
        Telegram.WebApp.sendData(new Date().toString());
    }

    function requestLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (position) {
                document.querySelector('#locationData').innerHTML = '(' + position.coords.latitude + ', ' + position.coords.longitude + ')';
            });
        } else {
            document.querySelector('#locationData').innerHTML = '(Geolocation is not supported in this browser)';
        }

        return false;
    }

    function requestVideo() {
        if (navigator.mediaDevices) {
            navigator.mediaDevices.getUserMedia({audio: false, video: true}).then(function (stream) {
                document.querySelector('#videoData').innerHTML = '(Access granted)';
            });
        } else {
            document.querySelector('#videoData').innerHTML = '(Media devices is not supported in this browser)';
        }
        return false;
    }

    function requestAudio() {
        if (navigator.mediaDevices) {
            navigator.mediaDevices.getUserMedia({audio: true, video: false}).then(function (stream) {
                document.querySelector('#audioData').innerHTML = '(Access granted)';
            });
        } else {
            document.querySelector('#audioData').innerHTML = '(Media devices is not supported in this browser)';
        }
        return false;
    }
</script>
</body>
</html>
