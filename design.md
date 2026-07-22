- min length in short url
- random kuchh chars generate

- tinyurl.com/yxbtz
- a-z, A-Z, 0-9 = total chars 62

- _, _ = 3844 shortcodes
- _, _, _ = 2,38,328 shortcodes
- _, _, _, _ = 1,47,76,336 shortcodes
- _, _, _, _, _ = 91,61,32,832 shortcodes
- _, _, _, _, _, _ = 56,80,02,35,584 ~= 56 Billion

- 56 Billion records
- 1 shortcode = 6 byte + long = 50 + 4 =  100 Byte * 56 Billion = 5.6TB  ~= 10tb

- 1. Shortening - Long URL Shorten
- 2. Redirection -> Short URL -> Long URL


Request
POST /api/links
body {"url":"https://www.amazon.in/...."}

Response
response 201
{
    "short_code": "https://tinyurl.com/t6sj9a6v"
}

Request
GET api/t6sj9a6v/

Response
response 302 temperory redirect
query shortcode -> long_url
click + 1
redirect(long_url)





