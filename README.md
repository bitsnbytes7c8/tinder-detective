Temporarily hosting this site <a href=http://bitsnbytes.pythonanywhere.com"> here </a>.

# tinder-detective
Stalk your friends on Tinder. Don't actually do that. It's just a description of what this code does.

You'll then need to answer "y" to a prompt asking you if you really want to look at your real-life friends' Tinder profiles. Otherwise the app will quit.
If you answer "y", the app will be available at `http://localhost:5000`.


Help it's not working
=====================
Listen pal you gotta put your Facebook id and Facebook auth token in SECRETS.json. I have no idea how to get these without sniffing the traffic of the Tinder app with mitmproxy. Or you can use any proxy, really. Or there's probably another way to do it. Or you could just close this page and go talk to them, I'm sure they're nice.

Ok, here's a really neat way to get it without messing with proxies (which I discovered after looking through a lot of github repos after I got tired making proxy to work on my Android phone):

Go to this URL : https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&state=%7B%22challenge%22%3A%22q1WMwhvSfbWHvd8xz5PT6lk6eoA%253D%22%2C%220_auth_logger_id%22%3A%2254783C22-558A-4E54-A1EE-BB9E357CC11F%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=54783C22-558A-4E54-A1EE-BB9E357CC11F#_=

If you've already authorized tinder, this would show a pop-up informing you the same. Open your chrome developer console now (or whatever is its equivalent in the browser you're using). Go to the 'Network' tab, and then click 'OK' to dismiss the pop-up. You'll see a call being made to "confirm?dpr=1" url. Copy its response to some text-editor, and then search for "access_token". That is your access token.

Getting your facebook id is easy enough, so you probably don't ned a description for that.

# Why did you make this?
¯\\\_(ツ)\_/¯
